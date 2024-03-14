FROM ubuntu:22.04
RUN apt-get update && \
    apt-get install -y python3 python3-pip && \
    pip install Flask hazelcast-python-client pyasyncore
EXPOSE 5000
COPY app.py .
ENTRYPOINT ["python3", "app.py"]
