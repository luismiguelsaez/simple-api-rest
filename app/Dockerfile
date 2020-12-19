FROM python:3.6-alpine

LABEL version="1.0"
LABEL description="Testing simple REST API"

EXPOSE 80

RUN mkdir /app
WORKDIR /app

COPY code .
COPY requirements.txt .

RUN pip install -r requirements.txt

ENTRYPOINT [ "flask","run","--host=0.0.0.0","--port=80" ]