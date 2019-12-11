FROM python:3.6

RUN ["pip", "install", "flask"]

RUN ["mkdir", "templates"]
RUN ["mkdir", "records"]

ADD templates /templates

COPY server3.py ./
COPY record.txt ./records/

CMD ["python", "server3.py"]
