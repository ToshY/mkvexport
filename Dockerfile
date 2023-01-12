FROM python:3.10-slim-buster AS dev

LABEL maintainer="ToshY (github.com/ToshY)"

ENV PIP_ROOT_USER_ACTION ignore

WORKDIR /app

RUN apt-get update \
    && apt install -y wget \
    && wget -O /usr/share/keyrings/gpg-pub-moritzbunkus.gpg https://mkvtoolnix.download/gpg-pub-moritzbunkus.gpg \
    && echo "deb [signed-by=/usr/share/keyrings/gpg-pub-moritzbunkus.gpg] https://mkvtoolnix.download/debian/ buster main" > /etc/apt/sources.list.d/mkvtoolnix.download.list \
    && echo "deb-src [signed-by=/usr/share/keyrings/gpg-pub-moritzbunkus.gpg] https://mkvtoolnix.download/debian/ buster main" >> /etc/apt/sources.list.d/mkvtoolnix.download.list \
    && apt-get update \
    && apt install -y mkvtoolnix

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt \
    && pip install --no-cache-dir --upgrade --force-reinstall 'setuptools>=65.5.1'

COPY . .

FROM dev AS prod

ENTRYPOINT ["python", "main.py"]
