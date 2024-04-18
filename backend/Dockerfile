FROM python:3.10.13-alpine3.19
WORKDIR /backend
COPY requirements.txt /backend
RUN pip install --no-cache-dir --upgrade pip -r requirements.txt
COPY . /backend
EXPOSE 8000
ENTRYPOINT ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]