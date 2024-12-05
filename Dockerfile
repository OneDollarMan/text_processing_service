FROM python:3.12

ENV PYTHONUNBUFFERED 1

WORKDIR /src

COPY requirements.txt src/requirements.txt
RUN pip3 install -r src/requirements.txt
RUN spacy download ru_core_news_sm

COPY /src/. /src