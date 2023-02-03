FROM python:3.10-slim-buster

WORKDIR /app

RUN apt-get install git

COPY requirements.txt /app

RUN pip3 install -r requirements.txt

COPY yashu.sh /app

CMD bash yashu.sh
