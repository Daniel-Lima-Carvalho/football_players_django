FROM python:3.7-slim-buster

WORKDIR /root/football_players_django

COPY ./ ./

RUN pip install -r requirements.txt

EXPOSE 8000
