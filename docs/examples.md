# Examples

The default behavior is to extract the attachments for an input file, to a subdirectory based on the name of said input file.

**Example**

Having a file `never-gonna-give-you-up.mkv` mounted to the `/app/input` directory will result in the following tree
structure after exporting the attachments.

```text
/app/input/
├── never-gonna-give-you-up.mkv
└── never-gonna-give-you-up/
    ├── attachments/
    │   ├── Arial.ttf
    │   ├── ...
    │   └── COMIC.ttf
    ├── chapters.xml
    ├── tags.xml
    ├── track4_eng.ass
    ├── ...
    └── track8_jpn.ass
```

## Basic

Add your files to the input directory of the mounted container.

```sh
docker run -it --rm \
  -u $(id -u):$(id -g) \
  -v ${PWD}/input:/app/input \
  ghcr.io/toshy/mkvexport:latest
```

By default, it will find all files from the `/app/input` directory (recursively) and write the output to a subdirectory based on the name of the input file.

## Specific file

Export attachments for a specific file.

```sh
docker run -it --rm \
  -u $(id -u):$(id -g) \
  -v ${PWD}/input:/app/input \
  ghcr.io/toshy/mkvexport:latest \
  -i "input/rick-astley-never-gonna-give-you-up.mkv"
```

## Specific subdirectory

Export attachments for a specific subdirectory.

```sh
docker run -it --rm \
  -u $(id -u):$(id -g) \
  -v ${PWD}/input:/app/input \
  ghcr.io/toshy/mkvexport:latest \
  -i "input/hits"
```

## Multiple inputs

Export attachments for files in multiple subdirectories.

```sh
docker run -it --rm \
  -u $(id -u):$(id -g) \
  -v ${PWD}/input:/app/input \
  ghcr.io/toshy/mkvexport:latest \
  -i "input/dir1" \
  -i "input/dir2" \
  -i "input/dir3" \
  -i "input/dir4" \
  -i "input/dir5"
```
