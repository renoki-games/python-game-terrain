ARG PYTHON_VERSION=3.8

FROM python:$PYTHON_VERSION

COPY . /usr/src/app

WORKDIR /usr/src/app

RUN pip install --no-cache-dir -r requirements.txt

CMD ["uvicorn", "server:app"]