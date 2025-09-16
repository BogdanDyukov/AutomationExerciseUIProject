FROM python:3.12-slim

WORKDIR /usr/workspace

COPY requirements.txt /usr/workspace

RUN pip install --upgrade pip && \
    pip install playwright && \
    playwright install --with-deps

RUN pip install -r requirements.txt