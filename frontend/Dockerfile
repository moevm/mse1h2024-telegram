FROM node:lts-alpine
RUN npm install -g http-server
WORKDIR /app
ARG VITE_TELEGRAM_BOT_NAME
ENV VITE_TELEGRAM_BOT_NAME=$VITE_TELEGRAM_BOT_NAME
COPY app/package*.json ./
RUN npm install
COPY ./app .
RUN npm run build
EXPOSE 8080
CMD [ "http-server", "dist" ]