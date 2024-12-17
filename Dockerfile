FROM python:3.9-slim

WORKDIR /app

COPY . /app
RUN pip install -r requirements.txt

CMD ["gunicorn", "--workers=2", "-b", "0.0.0.0:8000", "app:app"]