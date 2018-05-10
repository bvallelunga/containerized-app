FROM ubuntu:16.04
MAINTAINER Jay Karimi "jkarimi91@gmail.com"
RUN apt-get update -y && apt-get install -y python3-pip
COPY app/ /app
WORKDIR /app
RUN pip3 install -r requirements.txt
ENTRYPOINT ["python3"]
CMD ["rest_api.py"]
