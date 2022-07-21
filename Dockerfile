FROM python:3.10

WORKDIR /app

ENV PYTHONPATH /app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get update && \
    apt-get install -y --no-install-recommends gcc

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8000