FROM python:3.6

RUN ["pip", "install", "flask"]
RUN ["mkdir", "templates"]

ADD templates /templates

COPY server.py ./

EXPOSE 5001

CMD ["python", "server.py"]
