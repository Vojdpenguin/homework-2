FROM python:3.9-slim
WORKDIR /app
COPY . /app
ENV PYTHONPATH=/app
CMD ["python", "/app/Assistant/main.py"]
