FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --nocache-dir -r requirements.txt

COPY app.py .

EXPOSE 8081

CMD ["python", "app.py"]

