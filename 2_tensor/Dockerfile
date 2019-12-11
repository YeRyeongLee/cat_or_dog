FROM python:3.6

RUN ["pip", "install", "flask"]
RUN ["pip", "install", "tensorflow==1.5.0"]
RUN ["pip", "install", "numpy"]
RUN ["pip", "install", "matplotlib"]

RUN ["mkdir", "templates"]
RUN ["mkdir", "workspace"]
RUN ["mkdir", "uploads"]

ADD templates /templates
ADD workspace /workspace

COPY retrain.py ./
COPY server2.py ./

RUN ["python", "retrain.py", "--bottleneck_dir=./workspace/bottlenecks", "--model_dir=./workspace/inception", "--output_graph=./workspace/animals_graph.pb", "--output_labels=./workspace/animals_labels.txt", "--image_dir=./workspace/animals_photo", "--how_many_training_steps=1000"]

EXPOSE 5002

CMD ["python", "server2.py"]
