FROM python:3.10-slim

WORKDIR /app

# Requirements copy aur install karein
COPY app/requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Pura app folder (jis mein templates bhi hain) seedha copy karein
COPY app/ .

# Just to be 100% sure ke templates sahi copy hua hai
RUN ls -la /app && ls -la /app/templates

EXPOSE 5000

CMD ["python", "app.py"]
