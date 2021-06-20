ARG PYTHON_VERSION=3.7-alpine

FROM python:$PYTHON_VERSION

COPY . /usr/src/app

WORKDIR /usr/src/app

RUN apk upgrade --update && \
    apk add --virtual build-dependencies build-base gcc wget git zlib && \
    python3 -m ensurepip && \
    pip3 install --no-cache --upgrade pip setuptools && \
    python3 -m pip3 install -U --force-reinstall pip && \
    pip3 install --no-cache-dir -r requirements.txt && \
    rm -rf .git/ .github/ *.md && \
    apk --purge del build-dependencies && \
    rm -rf /var/cache/apk/*

EXPOSE 8000

CMD ["uvicorn", "server:app"]
