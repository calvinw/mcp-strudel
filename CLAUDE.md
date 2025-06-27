# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Common Commands

### Development Setup
- Install dependencies: `uv sync`
- Run as local MCP (STDIO): `uv run python strudel_server.py`
- Run as remote MCP (SSE): `uv run python sse_strudel_server.py`
- Run Chainlit web interface: `./run_chainlit.sh` or `uv run chainlit run -w app.py --host 0.0.0.0 --port 8082`

### Testing
No specific test framework is configured in this project.

## Architecture Overview

This is a Strudel live coding MCP (Model Context Protocol) server that enables Claude to send live coding patterns to a web-based Strudel REPL for real-time music generation.

### Core Components

**strudel_server.py** - Main MCP server using FastMCP framework
- Defines Strudel-specific MCP tools:
  - `play_code(session_id, code, description)` - Send Strudel code to specific browser session
  - `stop_play(session_id)` - Stop playback in specific session
  - `get_mcp_status(session_id)` - Check specific session status
  - `get_currently_playing_code(session_id)` - Get current editor code from browser
  - `get_strudel_docs()` - Access comprehensive Strudel documentation
  - `get_strudel_examples()` - Get curated code examples by category
  - `search_strudel_functions()` - Search function reference
- Session-based communication requiring specific session IDs (e.g. "fox8")
- Includes code validation to prevent dangerous patterns
- Integrates with Strudel documentation system for reference
- Entry point: `mcp.run()`

**sse_strudel_server.py** - HTTP/SSE wrapper combining MCP and UI
- Combines MCP server with UI app without duplication
- Provides SSE transport at `/sse` endpoint for MCP clients
- Mounts UI app at `/strudel` path for web interface
- Includes CORS middleware and OAuth metadata endpoint
- Shares WebSocket manager between MCP server and UI components

**ui_app.py** - Strudel web interface FastAPI app
- Separate FastAPI app for web interface and WebSocket handling
- Serves Strudel live coding interface with session ID injection
- WebSocket endpoint at `/ws` for real-time communication
- Connection manager handles session-based WebSocket connections
- Status endpoint for debugging connection state

**app.py** - Chainlit web interface for MCP tool testing
- Full web UI for testing MCP tools with OpenRouter LLM integration
- Supports multiple OpenRouter models (Google, Anthropic, OpenAI, etc.)
- Persistent user settings and tool buttons for quick testing
- Custom action callbacks for executing tools with sample parameters

### Shared Components

**shared_websocket.py** - WebSocket connection manager
- Reusable ConnectionManager class with session support
- Handles WebSocket lifecycle (connect, disconnect, broadcast)
- Session-based message routing with memorable session IDs (3 letters + 1 digit)
- Used by both MCP server and UI app for consistent WebSocket handling

### Static Web Interface

**static/index.html** - Strudel live coding web interface
- Embeds Strudel web components (`<strudel-repl>`)
- Session ID display and WebSocket connection status
- Sample pattern buttons organized by difficulty level
- Real-time pattern evaluation and playback
- Connection status indicators and message logging

### Configuration Files

**config.json** - MCP client configuration
- STDIO connection parameters for local MCP client connections
- Points to strudel_server.py as the command entry point
- Path needs updating to match current directory structure

**pyproject.toml** - Python dependencies
- Key dependencies: fastmcp, fastapi, uvicorn
- Uses uv for dependency management
- Workspace includes docs/ subdirectory

### Documentation System

**llm_docs/** - Strudel documentation integration
- `strudel_docs_system_v2.py` - Faithful librarian documentation system
- Provides complete access to Strudel website documentation
- Supports page retrieval, site navigation, and curated examples
- Used by MCP tools for comprehensive Strudel reference

### Integration Patterns

- Session-based architecture requiring explicit session IDs for all operations
- WebSocket manager shared between MCP server and UI app via `set_websocket_manager()`
- Strudel patterns validated before execution to prevent code injection
- Real-time bidirectional communication (send patterns, get current editor code)
- Comprehensive documentation integration for Strudel learning and reference