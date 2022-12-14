# Flip

[![Version](https://img.shields.io/docker/v/bn222/pl-flip?sort=semver)](https://hub.docker.com/r/bn222/pl-flip)
[![MIT License](https://img.shields.io/github/license/bn222/pl-flip)](https://github.com/bn222/pl-flip/blob/main/LICENSE)
[![ci](https://github.com/bn222/pl-flip/actions/workflows/ci.yml/badge.svg)](https://github.com/bn222/pl-flip/actions/workflows/ci.yml)

`pl-flip` is a [_ChRIS_](https://chrisproject.org/)
_ds_ plugin which takes in images  as input files and
creates flipped images as output files.

## Abstract

Simple tool to flip images vertically or horizontally as specified
by argument

## Installation

`pl-flip` is a _[ChRIS](https://chrisproject.org/) plugin_, meaning it can
run from either within _ChRIS_ or the command-line.

[![Get it from chrisstore.co](https://ipfs.babymri.org/ipfs/QmaQM9dUAYFjLVn3PpNTrpbKVavvSTxNLE5BocRCW1UoXG/light.png)](https://chrisstore.co/plugin/pl-flip)

## Local Usage

To get started with local command-line usage, use [Apptainer](https://apptainer.org/)
(a.k.a. Singularity) to run `pl-flip` as a container:

```shell
singularity exec docker://bn222/pl-flip flip [--args values...] input/ output/
```

To print its available options, run:

```shell
singularity exec docker://bn222/pl-flip flip --help
```

## Examples

`flip` requires three positional arguments: a direction
(set to `horizontal`, `vertical` or `both`), a directory
containing input data, and a directory where to create
output data. First, create the input directory and move
input data into it.

```shell
mkdir incoming/ outgoing/
mv some.dat other.dat incoming/
singularity exec docker://bn222/pl-flip:latest flip DIRECTION incoming/ outgoing/
```

### Building

Build a local container image:

```shell
docker build -t localhost/bn222/pl-flip .
```

### Running

Mount the source code `flip.py` into a container to try out changes without rebuild.
The argument "both" can be replaced by "horizontal" or "vertical".

```shell
docker run --rm -it --userns=host -u $(id -u):$(id -g) \
    -v $PWD/flip.py:/usr/local/lib/python3.10/site-packages/flip.py:ro \
    -v $PWD/in:/incoming:ro -v $PWD/out:/outgoing:rw -w /outgoing \
    localhost/bn222/pl-flip flip both /incoming /outgoing
```

### Testing

Run unit tests using `pytest`.
It's recommended to rebuild the image to ensure that sources are up-to-date.
Use the option `--build-arg extras_require=dev` to install extra dependencies for testing.

```shell
docker build -t localhost/bn222/pl-flip:dev --build-arg extras_require=dev .
docker run --rm -it localhost/bn222/pl-flip:dev pytest
```

## Release

Steps for release can be automated by [Github Actions](.github/workflows/ci.yml).
This section is about how to do those steps manually.

### Increase Version Number

Increase the version number in `setup.py` and commit this file.

### Push Container Image

Build and push an image tagged by the version. For example, for version `1.2.3`:

```
docker build -t docker.io/bn222/pl-flip:1.2.3 .
docker push docker.io/bn222/pl-flip:1.2.3
```

### Get JSON Representation

Run [`chris_plugin_info`](https://github.com/bn222/chris_plugin#usage)
to produce a JSON description of this plugin, which can be uploaded to a _ChRIS Store_.

```shell
docker run --rm localhost/bn222/pl-flip:dev chris_plugin_info > chris_plugin_info.json
```

