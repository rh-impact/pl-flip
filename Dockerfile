# Python version can be changed, e.g.
# FROM python:3.8
# FROM docker.io/fnndsc/conda:python3.10.2-cuda11.6.0
FROM docker.io/python:3.10.6-slim-bullseye

LABEL org.opencontainers.image.authors="bn222 <bnemeth@redhat.com>" \
      org.opencontainers.image.title="Flip" \
      org.opencontainers.image.description="A ChRIS plugin to flip images horizontally, vertically or both"

WORKDIR /usr/local/src/pl-flip

RUN apt update && apt-get -y install imagemagick

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .
ARG extras_require=none
RUN pip install ".[${extras_require}]"

CMD ["flip", "--help"]
