FROM python:3.9-slim

WORKDIR /app

COPY . /app

RUN pip install fyers-apiv3 python-dotenv

CMD ["python", "fyersacceskey.py"]
