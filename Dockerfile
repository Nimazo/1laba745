FROM debian:latest
RUN mkdir /lab
COPY . /lab
RUN apt-get update && apt-get install -y apt-transport-https
RUN apt-get install -y python3
RUN python3 /lab/Raise.py 
