FROM node:21-alpine as develop
WORKDIR /app
ARG VITE_TELEGRAM_BOT_NAME
ENV VITE_TELEGRAM_BOT_NAME=$VITE_TELEGRAM_BOT_NAME
COPY app/package*.json .
RUN npm install
COPY ./app .

FROM develop as builder
RUN npm run build

FROM alpine:3.19 as deploy

RUN apk add nginx && \
    rm -rf /var/cache/apk/*

RUN chown 1001:1001 -R /var/lib/nginx /var/log/nginx /run/nginx

COPY --from=builder /app/dist /usr/share/nginx/html
COPY nginx.conf /etc/nginx/nginx.conf
USER 1001

CMD [ "nginx", "-g", "daemon off;" ]