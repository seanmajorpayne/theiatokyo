FROM python:3.8.5-slim

RUN apt-get update

WORKDIR /app

COPY . .

RUN pip3 install --upgrade pip && \
    pip3 install --no-cache-dir -r requirements.txt

EXPOSE 80

CMD ["flask run"]