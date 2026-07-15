FROM python:3.10-slim

WORKDIR /app

# Install Python dependencies
COPY app/requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# Copy all application files
COPY app/ .

EXPOSE 5000

CMD ["python", "app.py"]
