FROM python:3.10.13-alpine3.19
WORKDIR /tg_bot
RUN pip install --no-cache-dir --upgrade pip
RUN pip install python-telegram-bot aio_pika
COPY . /tg_bot
ENTRYPOINT ["python3", "bot/main.py"]