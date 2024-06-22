<h1 align="center"> 📺 MKVexport </h1>

<div align="center">
    <img src="https://img.shields.io/github/v/release/toshy/mkvexport?label=Release&sort=semver" alt="Current bundle version" />
    <img src="https://img.shields.io/github/actions/workflow/status/toshy/mkvexport/codestyle.yml?branch=main&label=Black" alt="Black">
    <img src="https://img.shields.io/github/actions/workflow/status/toshy/mkvexport/codequality.yml?branch=main&label=Ruff" alt="Ruff">
    <img src="https://img.shields.io/github/actions/workflow/status/toshy/mkvexport/statictyping.yml?branch=main&label=Mypy" alt="Mypy">
    <img src="https://img.shields.io/github/actions/workflow/status/toshy/mkvexport/security.yml?branch=main&label=Security%20check" alt="Security check" />
</div>

## 📝 Quickstart

A command-line utility for extracting attachments (subtitles, fonts and chapters) of MKV files.

## 🧰 Requirements

* 🐋 [Docker](https://docs.docker.com/get-docker/)

## 🎬 Usage

MKVexport requires 1 volume to be mounted: `/app/input`.

### 🐋 Docker

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
      - ./input:/input
```

Then run it.

```shell
docker compose run -u $(id -u):$(id -g) --rm mkvexport -h
```

## 📚 Examples

Extracted file attachments will always be put into a newly created directory based on the filename of the input file.

```text
|-- never-gonna-give-you-up.mkv
|-- never-gonna-give-you-up
    |-- attachments
        |-- Arial.ttf
        |-- ...
        |-- COMIC.TTF  
    |-- chapters.xml
    |-- tags.xml
    |-- track4_eng.ass
    |-- ...
    |-- track8_jpn.ass
```

In the above example, our file `never-gonna-give-you-up.mkv`, will yield a directory named `never-gonna-give-you-up`.
This directory will contain a chapters file `chapters.xml`, a tags file `tags.xml`, subtitles (which are named in the
format `track{id}_{iso639-3}.{extension}`) and a subdirectory `attachments` containing the fonts.

### Arguments

#### Default

When no arguments are provided, MKVexport will automatically export attachments for all files mounted to the `/app/input` directory.

#### Subdirectory

Let's say you have some files in a subdirectory called `latest-hits` (`./rick-astley/latest-hits`) and you want to extract attachments 
for just those files.

```shell
docker run -it --rm \
  -u $(id -u):$(id -g) \
  -v ${PWD}/rick-astley:/app/input \
  ghcr.io/toshy/mkvexport:latest \
  -i "latest-hits"
```

#### File

Let's say you have a file called `never-gonna-give-you-up.mkv` (`./rick-astley/never-gonna-give-you-up.mkv`) and you want to extract attachments 
for just that file

```shell
docker run -it --rm \
  -u $(id -u):$(id -g) \
  -v ${PWD}/rick-astley:/app/input \
  ghcr.io/toshy/mkvexport:latest \
  -i "never-gonna-give-you-up.mkv"
```

## 🛠️ Contribute

### Requirements

* ☑️ [Pre-commit](https://pre-commit.com/#installation).
* 🐋 [Docker Compose V2](https://docs.docker.com/compose/install/)
* 📋 [Task 3.37+](https://taskfile.dev/installation/)

### Pre-commit

Setting up `pre-commit` code style & quality checks for local development.

```shell
pre-commit install
```

## ❕ License

This repository comes with a [MIT license](./LICENSE).
