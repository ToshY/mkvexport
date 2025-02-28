<h1 align="center"> 📺 MKVexport </h1>

<div align="center">
    <img src="https://img.shields.io/github/v/release/toshy/mkvexport?label=Release&sort=semver" alt="Current bundle version" />
    <img src="https://img.shields.io/github/actions/workflow/status/toshy/mkvexport/codestyle.yml?branch=main&label=Black" alt="Black">
    <img src="https://img.shields.io/github/actions/workflow/status/toshy/mkvexport/codequality.yml?branch=main&label=Ruff" alt="Ruff">
    <img src="https://img.shields.io/github/actions/workflow/status/toshy/mkvexport/statictyping.yml?branch=main&label=Mypy" alt="Mypy">
    <img src="https://img.shields.io/github/actions/workflow/status/toshy/mkvexport/security.yml?branch=main&label=Security%20check" alt="Security check" />
    <br /><br />
    <div>A command-line utility for extracting attachments (subtitles, fonts and chapters) of MKV files.</div>
</div>

## 📝 Quickstart

```sh
docker run -it --rm \
  -u $(id -u):$(id -g) \
  -v ${PWD}/input:/app/input \
  ghcr.io/toshy/mkvexport:latest -h
```

## 📜 Documentation

The documentation is available at [https://toshy.github.io/mkvexport](https://toshy.github.io/mkvexport).

## 🛠️ Contribute

### Requirements

* ☑️ [Pre-commit](https://pre-commit.com/#installation).
* 🐋 [Docker Compose V2](https://docs.docker.com/compose/install/)
* 📋 [Task 3.37+](https://taskfile.dev/installation/)

## ❕ License

This repository comes with a [MIT license](./LICENSE).
