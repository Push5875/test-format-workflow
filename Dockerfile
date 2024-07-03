FROM python:3

WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python","app.py","--host=0.0.0.0"]

EXPOSE 5000