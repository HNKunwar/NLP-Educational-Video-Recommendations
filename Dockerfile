FROM python:3.8-slim

WORKDIR /app

COPY requirements.txt /app

RUN pip install --no-cache-dir -r requirements.txt
RUN python -m nltk.downloader punkt
RUN pip install gunicorn
RUN pip install -U flask-cors

COPY api /app/api

EXPOSE 80

WORKDIR /app/api

CMD ["gunicorn", "--workers=3", "--bind", "0.0.0.0:80", "index:app"]