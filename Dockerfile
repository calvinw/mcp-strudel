# Use Python 3.13 slim image (project requires >=3.13)
FROM python:3.13-slim

# Set working directory
WORKDIR /app

# Install uv for dependency management
RUN pip install uv

# Copy dependency files
COPY pyproject.toml .
COPY uv.lock .

# Install dependencies using uv
RUN uv sync --frozen

# Copy all Python server files
COPY strudel_server.py .
COPY sse_strudel_server.py .
COPY ui_app.py .
COPY shared_websocket.py .

# Copy static files for the web interface
COPY static/ ./static/

# Copy documentation directories
COPY docs_processed/ ./docs_processed/
COPY llm_docs/ ./llm_docs/

# Expose port 8080 (Cloud Run default)
EXPOSE 8080

# Set environment variable for port
ENV PORT=8080

# Run the server using uv
CMD ["uv", "run", "python", "sse_strudel_server.py"]
