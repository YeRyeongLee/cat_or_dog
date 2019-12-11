FROM python:3.6

RUN ["pip", "install", "flask"]

RUN ["mkdir", "records"]

COPY server0.py ./

CMD ["python", "server0.py"]
