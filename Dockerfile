FROM ubuntu:latest

WORKDIR /app

COPY requirements.txt /app

RUN pip3 install -r requirements.txt

COPY yashu.sh /app

CMD bash yashu.sh
