# AI-KungFU East Africa MCP Server
# Glama-compatible Dockerfile for historia-mcp
FROM python:3.12-slim

LABEL org.opencontainers.image.source="https://github.com/gabrielmahia/historia-mcp"
LABEL org.opencontainers.image.description="historia-mcp — East Africa AI Coordination Infrastructure"
LABEL org.opencontainers.image.licenses="MIT"

RUN pip install --no-cache-dir historia-mcp

CMD ["historia-mcp"]
