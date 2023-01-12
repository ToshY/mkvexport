<h1 align="center"> 🛠️ MKVextract Subs </h1>

<div align="center">
    <img src="https://img.shields.io/github/v/release/toshy/mkvextract-subs?label=Release&sort=semver" alt="Current bundle version" />
    <a href="https://hub.docker.com/r/t0shy/mkvextract-subs"><img src="https://img.shields.io/badge/Docker%20Hub-t0shy%2Fmkvextract-subs-blue" alt="Docker Hub" /></a>
    <img src="https://img.shields.io/github/actions/workflow/status/toshy/mkvextract-subs/pylint.yml?branch=main&label=Pylint" alt="Code style">
    <img src="https://img.shields.io/badge/Code%20Style-PEP8-orange.svg" alt="Code style" />
    <img src="https://img.shields.io/github/actions/workflow/status/toshy/mkvextract-subs/security.yml?branch=main&label=Security%20check" alt="Security check" />
    <br /><br />
</div>

## 📝 Quickstart

This tool will extract subtitle tracks, attachments, chapters and tags for your MKV files.

## 🧰 Requirements

* [🐋 Docker](https://docs.docker.com/get-docker/)

## 🎬 Usage

1. Pull the image.

```shell
docker pull t0shy/mkvextract-subs:latest
```

2. Run it.

Default behaviour is to extract the info for all MKV files found (recursively) in the mounted directory.

```shell
docker run -it --rm \
  -u $(id -u):$(id -g) \
  -v ${PWD}/rick-astley:/input \
  t0shy/mkvextract-subs:latest
```

> Note: please make sure to mount to the `/input` directory on the container.

If you only want to extract info for a single file, or files in a subdirectory, you can pass that as an argument (`-i`) to the
container.

* Subdirectory `rick-astley/latest-hits`

```shell
docker run -it --rm \
  -u $(id -u):$(id -g) \
  -v ${PWD}/rick-astley:/input \
  t0shy/mkvextract-subs:latest \
  -i "latest-hits"
```

* File `rick-astley/never-gonna-give-you-up.mkv`

```shell
docker run -it --rm \
  -u $(id -u):$(id -g) \
  -v ${PWD}/rick-astley:/input \
  t0shy/mkvextract-subs:latest \
  -i "never-gonna-give-you-up.mkv"
```

3. Check the result.

The extracted info will always be put into a newly created directory based on the filename of the input file.

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

## 🛠️ Contribute

### Prerequisites

* Pre-commit
    * See the pre-commit [installation guide](https://pre-commit.com/#installation) to get started.
* Docker Compose
    * See the Docker Compose [installation guide](https://docs.docker.com/compose/install/) to get started.
* Task
    * See the Task [installation guide](https://taskfile.dev/installation/) to get started.

### Pre-commit

Setting up `pre-commit` code style & quality checks for local development.

```shell
pre-commit install
```

### Checks

```shell
task contribute
```

> Note: you can use `task tools:black:fix` to resolve codestyle issues.

## ❕ License

This repository comes with a [MIT license](./LICENSE).
