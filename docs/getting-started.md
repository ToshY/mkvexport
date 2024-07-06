## Requirements

- 🐋 [Docker](https://docs.docker.com/get-docker/)

## Pull image

```shell
docker pull ghcr.io/toshy/mkvexport:latest
```

## Run container

### 🐋 Docker

Run with `docker`.

```shell
docker run -it --rm \
  -u $(id -u):$(id -g) \
  -v ${PWD}/input:/app/input \
  ghcr.io/toshy/mkvexport:latest -h
```

### 🐳 Compose

Create a `compose.yaml` file.

```yaml
services:
  mkvexport:
    image: ghcr.io/toshy/mkvexport:latest
    volumes:
      - ./input:/app/input
```

Run with `docker compose`.

```shell
docker compose run -u $(id -u):$(id -g) --rm mkvexport -h
```

## Volumes

The following volume mounts are **required**: 

- `/app/input`
