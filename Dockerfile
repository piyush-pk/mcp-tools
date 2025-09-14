FROM ghcr.io/astral-sh/uv:python3.13-bookworm

WORKDIR /app
COPY requirements.txt .

RUN uv venv

# Install deps inside container
RUN uv pip install -r requirements.txt

COPY . .

ENV ROOT_DIR=/app/sandbox
RUN mkdir -p /app/sandbox

# Default: listen on all interfaces, port 8000
ENV MCP_HOST=0.0.0.0
ENV MCP_PORT=8000

EXPOSE 8000

CMD ["uv", "run", "main.py"]
