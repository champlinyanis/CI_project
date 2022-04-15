FROM ubuntu:latest

RUN apt-get update

RUN apt-get install python3 -y
RUN apt-get install python3-pip -y
RUN apt-get install numpy

WORKDIR /test

COPY . .

CMD ["python3", "main.py"]