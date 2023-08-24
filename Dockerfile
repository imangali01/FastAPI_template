FROM python:3.8

RUN mkdir /fastapi_app

WORKDIR /fastapi_app

COPY . .

RUN python -m pip install --upgrade pip && \
    pip install -r requirements.txt