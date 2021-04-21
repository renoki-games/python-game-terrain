ARG PYTHON_VERSION=3.7-alpine

FROM python:$PYTHON_VERSION

COPY . /usr/src/app

WORKDIR /usr/src/app

RUN pip install --no-cache-dir -r requirements.txt && \
    rm -rf .git/ .github/ *.md

CMD ["uvicorn", "server:app"]
