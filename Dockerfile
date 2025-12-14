# STAGE 1: Builder (Installs tools and dependencies)
FROM python:3.12-slim-bookworm AS builder

# Install uv binary
COPY --from=ghcr.io/astral-sh/uv:latest /uv /bin/uv

WORKDIR /app

# Copy config files
COPY pyproject.toml uv.lock ./

# Install dependencies to a local folder (.venv)
# --frozen: strict install from lockfile
# --no-dev: don't install pytest/ruff in production
RUN uv sync --frozen --no-install-project --no-dev

# STAGE 2: Runner (The clean, final image)
FROM python:3.12-slim-bookworm

WORKDIR /app

# Copy the virtual environment from the builder
COPY --from=builder /app/.venv /app/.venv

# Copy the application code
COPY . .

# Add virtualenv to PATH
ENV PATH="/app/.venv/bin:$PATH"

# Run the app on port 8080
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]