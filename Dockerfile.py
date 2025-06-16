# Dockerfile.py
# image for Debian Linux OS
FROM debian:stable-slim
# Copy bookbot to container
COPY main.py main.py
# Copy the .txt file to the container
COPY books/ books/
# Run the container, then close
CMD ["python", "main.py"]