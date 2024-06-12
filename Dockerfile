FROM python:3.8-slim

COPY reader.py /app/reader.py

WORKDIR /app

CMD ["python", "reader.py"]
