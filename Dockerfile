ARG PYTHON_VERSION=3.7

FROM python:$PYTHON_VERSION

COPY . /usr/src/app

WORKDIR /usr/src/app

RUN python3 -m ensurepip && \
    pip3 install --no-cache --upgrade pip setuptools && \
    pip3 install --no-cache-dir -r requirements.txt

EXPOSE 8000

CMD ["uvicorn", "server:app"]