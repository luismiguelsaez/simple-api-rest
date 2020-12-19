FROM python:3.6-alpine

LABEL version="1.0"
LABEL description="Test execution against simple REST API"

RUN mkdir /app
WORKDIR /app

COPY code .
COPY requirements.txt .

RUN pip install -r requirements.txt

ENTRYPOINT [ "pytest","main.py" ]