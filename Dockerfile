# Use the official Python lightweight image
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Install system dependencies required for OpenCV and deepface
# We clean up the apt cache to keep the image size minimal
RUN apt-get update && apt-get install -y --no-install-recommends \
    libgl1 \
    libglib2.0-0 \
    && rm -rf /var/lib/apt/lists/*

# Copy the requirements file first to leverage Docker layer caching
COPY requirements.txt .

# Install python dependencies
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Create a non-root user and home directory for security
# DeepFace will download its weights to the home directory
ENV HOME=/home/appuser
RUN useradd -m -d $HOME appuser \
    && chown -R appuser:appuser /app $HOME

# Switch to the non-root user
USER appuser

# Optional: Pre-download DeepFace ML weights during the build stage
# This optimizes the image so the first API request doesn't stall while downloading.
RUN python -c "from deepface import DeepFace; DeepFace.build_model('Age')" || true

# Copy application files (with correct permissions)
COPY --chown=appuser:appuser main.py .
COPY --chown=appuser:appuser app/ ./app/

# Expose port for FastAPI
EXPOSE 8000

# Command to run the application
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
