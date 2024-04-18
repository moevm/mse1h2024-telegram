FROM python:3.10.13-alpine3.19
WORKDIR /tg_bot
RUN pip install --no-cache-dir --upgrade pip
COPY ./requirements.txt /tg_bot
RUN pip install -r requirements.txt
COPY . /tg_bot
ENTRYPOINT ["python3", "-m", "bot.main"]