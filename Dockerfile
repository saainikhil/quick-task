FROM python:3.10-slim

WORKDIR /app

COPY app.py .
RUN pip install flask gunicorn

EXPOSE 5000

CMD sh -c "gunicorn -b 0.0.0.0:$PORT app:app"
