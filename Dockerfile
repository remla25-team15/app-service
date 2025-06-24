# Stage 1: Build stage with all dependencies needed for building/installing
FROM python:3.10-slim AS builder

WORKDIR /app

# Install build dependencies
RUN apt-get update && apt-get install -y \
    git \
    gcc \
    build-essential \
    libopenblas-dev \
    libffi-dev \
    libssl-dev \
    python3-dev \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .

# Install Python dependencies into a separate directory to copy later
RUN pip install --prefix=/install -r requirements.txt

COPY . .

# Stage 2: Final minimal image
FROM python:3.10-slim

WORKDIR /app

# Copy only the installed packages from the builder image
COPY --from=builder /install /usr/local

# Copy app source code
COPY --from=builder /app /app

EXPOSE 5000

CMD ["python", "run.py"]
