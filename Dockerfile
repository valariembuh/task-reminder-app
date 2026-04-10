i<<<<<<< HEAD
FROM maven:3.9.9-eclipse-temurin-17

WORKDIR /app

COPY . .

RUN mvn clean package

CMD ["mvn","exec:java"]
=======
FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8080

CMD ["python", "app.py"]

