FROM python:3.12-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY scheduler.py .
COPY twc_token /root/.twcrc
CMD ["python", "scheduler.py"]
