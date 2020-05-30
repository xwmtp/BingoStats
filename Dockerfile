FROM python:3.8-slim-buster

COPY ./ /etc/BingoStats

RUN pip install dash dash_core_components pandas requests

VOLUME ["/etc/BingoStats/logs", "/etc/BingoStats/BingoBoards/Versions"]

EXPOSE 80

WORKDIR /etc/BingoStats
CMD ["python", "Main.py", "0.0.0.0", "False"]
