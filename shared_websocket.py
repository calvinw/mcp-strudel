"""
Shared WebSocket Connection Manager for MCP UI Servers

This module provides a reusable ConnectionManager class that can be used
across different MCP server implementations to handle WebSocket connections
with session support.
"""

import logging
import random
import string
from typing import List, Dict
from fastapi import WebSocket

# Configure logging
logger = logging.getLogger(__name__)


class ConnectionManager:
    """WebSocket connection manager with session support"""
    
    def __init__(self):
        self.active_connections: List[WebSocket] = []
        self.session_connections: Dict[str, WebSocket] = {}  # session_id -> websocket

    async def connect(self, websocket: WebSocket, session_id: str = None):
        """Accept a WebSocket connection and optionally associate it with a session"""
        await websocket.accept()
        self.active_connections.append(websocket)
        if session_id:
            self.session_connections[session_id] = websocket
            logger.info(f"New WebSocket connection with session {session_id}. Total: {len(self.active_connections)}")
        else:
            logger.info(f"New WebSocket connection. Total: {len(self.active_connections)}")

    def disconnect(self, websocket: WebSocket):
        """Remove a WebSocket connection and clean up session associations"""
        if websocket in self.active_connections:
            self.active_connections.remove(websocket)
        
        # Remove from session connections
        session_to_remove = None
        for session_id, ws in self.session_connections.items():
            if ws == websocket:
                session_to_remove = session_id
                break
        
        if session_to_remove:
            del self.session_connections[session_to_remove]
            logger.info(f"WebSocket disconnected (session {session_to_remove}). Total: {len(self.active_connections)}")
        else:
            logger.info(f"WebSocket disconnected. Total: {len(self.active_connections)}")

    async def send_to_session(self, session_id: str, message: str) -> bool:
        """Send message to specific session. Returns True if successful."""
        if session_id in self.session_connections:
            try:
                await self.session_connections[session_id].send_text(message)
                return True
            except Exception as e:
                logger.error(f"Error sending to session {session_id}: {e}")
                self.disconnect(self.session_connections[session_id])
                return False
        else:
            return False
    
    def has_connections(self) -> bool:
        """Check if there are any active connections"""
        return len(self.active_connections) > 0
    
    def get_connection_count(self) -> int:
        """Get the number of active connections"""
        return len(self.active_connections)
    
    async def broadcast(self, message: str):
        """Send message to all connected clients"""
        disconnected = []
        for connection in self.active_connections:
            try:
                await connection.send_text(message)
            except Exception as e:
                logger.error(f"Error broadcasting to connection: {e}")
                disconnected.append(connection)
        
        # Remove disconnected clients
        for connection in disconnected:
            self.disconnect(connection)
    
    def generate_session_id(self) -> str:
        """Generate a memorable 4-character session ID (3 letters + 1 digit)"""
        while True:
            letters = ''.join(random.choices(string.ascii_lowercase, k=3))
            digit = random.choice(string.digits)
            session_id = letters + digit
            # Ensure it's not already in use
            if session_id not in self.session_connections:
                return session_id
    
    def get_session_ids(self) -> List[str]:
        """Get list of active session IDs"""
        return list(self.session_connections.keys())

