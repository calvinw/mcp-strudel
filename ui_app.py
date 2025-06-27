"""
Strudel UI FastAPI App - Separate from MCP server
Provides web interface, WebSocket, and static file serving
"""

import sys
from pathlib import Path
from fastapi import FastAPI, Request, WebSocket, WebSocketDisconnect
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
import json
import logging

# Add parent directory for shared modules
sys.path.append(str(Path(__file__).parent.parent))
from shared_websocket import ConnectionManager

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Create UI FastAPI app
ui_app = FastAPI(title="Strudel UI")

# Create WebSocket manager
manager = ConnectionManager()

# Import strudel server functions for WebSocket handling
from strudel_server import set_websocket_manager, handle_code_response
set_websocket_manager(manager)

# Mount static files
static_dir = Path(__file__).parent / "static"
ui_app.mount("/static", StaticFiles(directory=str(static_dir)), name="static")

# UI route
@ui_app.get("/")
async def serve_strudel_player(request: Request):
    """Serve the Strudel live coding interface with session ID"""
    session_id = manager.generate_session_id()
    
    # Read the HTML template
    html_path = Path(__file__).parent / "static" / "index.html"
    html_content = open(html_path, "r").read()
    
    # Inject session ID into the HTML
    html_content = html_content.replace(
        '<!-- SESSION_ID_PLACEHOLDER -->', 
        f'<script>window.sessionId = "{session_id}";</script>'
    )
    
    # Update WebSocket URL to use current path + /ws
    html_content = html_content.replace(
        '/ws?session_id=',
        f'{request.url.path}ws?session_id=' if request.url.path.endswith('/') else f'{request.url.path}/ws?session_id='
    )
    
    return HTMLResponse(content=html_content)

# WebSocket endpoint
@ui_app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    """WebSocket endpoint for real-time communication with the Strudel player"""
    session_id = websocket.query_params.get('session_id')
    logger.info(f"Strudel WebSocket connection attempt with session_id='{session_id}'")
    
    await manager.connect(websocket, session_id)
    
    try:
        while True:
            data = await websocket.receive_text()
            try:
                message = json.loads(data)
                if message.get("type") == "ping":
                    await websocket.send_text(json.dumps({"type": "pong"}))
                elif message.get("type") == "current-code-response":
                    request_id = message.get("request_id", "")
                    current_code = message.get("code", "")
                    if request_id:
                        handle_code_response(request_id, current_code)
                elif message.get("type") == "evaluation-error":
                    error_msg = message.get("error", "Unknown error")
                    code_snippet = message.get("code", "Unknown code")
                    logger.error(f"Strudel evaluation error: {error_msg} | Code: {code_snippet}")
            except json.JSONDecodeError:
                logger.warning(f"Invalid JSON received: {data}")
    except WebSocketDisconnect:
        manager.disconnect(websocket)
    except Exception as e:
        logger.error(f"Strudel WebSocket error: {e}")
        manager.disconnect(websocket)

# Debug endpoints
@ui_app.get("/status")
async def get_status():
    """Get status of WebSocket connections"""
    return {
        "total_connections": manager.get_connection_count(),
        "active_sessions": manager.get_session_ids()
    }