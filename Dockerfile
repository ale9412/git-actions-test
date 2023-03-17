FROM python:latest

# Set working directory
WORKDIR /app

# Copy script
COPY . /app


# start the server
CMD ["python3", "server.py"]

EXPOSE 8000

