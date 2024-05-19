FROM node:21-alpine as develop
WORKDIR /app
COPY app/package*.json .
RUN npm install
COPY ./app .

FROM develop as builder
ARG VITE_BACKEND_URL
ENV VITE_BACKEND_URL=$VITE_BACKEND_URL
RUN npm run build

FROM nginx:1.25.5 as deploy

COPY --from=builder /app/dist /usr/share/nginx/html

COPY nginx.conf /etc/nginx/nginx.conf

CMD [ "nginx", "-g", "daemon off;" ]