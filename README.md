
# Consumer of Fake Sensor Data for Juseong

This is a small example script to pull data from the [Fake Sensor API](https://github.com/TheBeege/juseong-fake-sensors/).

I recommend you fork repository this to work on your own project.

## Setup

Normal Python project setup on Linux/MacOS/WSL:

```shell
python -m venv .venv
source .venv/bin/activate
pip install -e ".[dev]"
```

## Usage

First, make sure you have [Docker installed](https://docs.docker.com/desktop/) or
[Rancher](https://rancherdesktop.io/) with the Docker CLI.

Run the fake sensor via docker-compose:

```shell
docker-compose up
```

Add a `-d` for running in the background if you prefer. Don't forget to cleanup if you do this!

Then open up your browser to the [Swagger docs page](http://127.0.0.1:8000/docs)

## Cleanup

```shell
docker-compose down
```
