# syntax=docker/dockerfile:1
FROM python:3.10
WORKDIR /app
COPY . .
CMD ["python3","main.py"] 
