"""
Strudel SSE Server - Matching button state example structure
"""

import os
import sys
from pathlib import Path
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse, RedirectResponse
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
import logging
from strudel_server import mcp, set_websocket_manager

# Add parent directory to path for shared modules
sys.path.append(str(Path(__file__).parent.parent))
from shared_websocket import ConnectionManager

# Import the UI app
from ui_app import ui_app, manager as ui_manager

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Set the UI manager as the MCP server's WebSocket manager
set_websocket_manager(ui_manager)

# Create the ASGI app for MCP
http_app = mcp.http_app(transport="sse")

# Minimal OAuth endpoint (just enough for Claude.ai)
async def oauth_metadata(request: Request):
    base_url = str(request.base_url).rstrip("/")
    return JSONResponse({
        "issuer": base_url
    })

# Create main FastAPI app
app = FastAPI(title="Strudel MCP Server with UI")

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["GET", "POST", "OPTIONS", "PUT", "DELETE"],
    allow_headers=["Content-Type", "Authorization", "x-api-key", "Upgrade", "Connection", "Sec-WebSocket-Key", "Sec-WebSocket-Version", "Sec-WebSocket-Protocol"],
    expose_headers=["Content-Type", "Authorization", "x-api-key"],
    max_age=86400
)

# Add the OAuth metadata route
app.add_api_route("/.well-known/oauth-authorization-server", oauth_metadata, methods=["GET"])

# Add redirect for /strudel to /strudel/ (must be before mount)
@app.get("/strudel")
async def redirect_to_strudel():
    return RedirectResponse(url="/strudel/", status_code=307)

# Mount UI app first (specific routes)
app.mount("/strudel", ui_app)

# Mount MCP server at root
app.mount("/", http_app)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    print(f"""
🎵 Strudel MCP Server Starting on port {port}!

🌐 Web Interface: http://localhost:{port}/strudel/
🤖 MCP Endpoint: http://localhost:{port}/sse
⚡ WebSocket: http://localhost:{port}/strudel/ws
📊 Status: http://localhost:{port}/api/status

Ready for both web browsers and Claude integration! 🎯
    """)
    uvicorn.run(app, host="0.0.0.0", port=port)