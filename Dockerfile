ARG PYTHON_VERSION=3.7-alpine

FROM python:$PYTHON_VERSION

COPY . /usr/src/app

WORKDIR /usr/src/app

RUN apk upgrade --update && \
    apk add --no-cache --update build-base && \
    pip install -U setuptools pip && \
    pip install --no-cache-dir -r requirements.txt && \
    rm -rf .git/ .github/ *.md && \
    apk del build-base && \
    rm -rf /var/cache/apk/*

CMD ["uvicorn", "server:app"]
