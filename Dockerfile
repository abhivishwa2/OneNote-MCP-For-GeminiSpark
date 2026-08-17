# Use the official Python slim image
FROM python:3.13-slim

# Install the uv package manager
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

# Copy your local server files into the container
COPY . /app
WORKDIR /app

# Ensure logs appear immediately in Google Cloud Logs
ENV PYTHONUNBUFFERED=1

# Install project dependencies
RUN uv sync

# Expose the port Cloud Run uses to send traffic
EXPOSE 8080

# Run the server (Ensure arguments match your server's HTTP/SSE command)
CMD ["uv", "run", "onenote-mcp-server"]