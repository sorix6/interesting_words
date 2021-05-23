FROM python:3.7.10-slim

WORKDIR /usr/src/app

COPY ./requirements.txt /usr/src/app
COPY ./files /usr/src/files

RUN pip install --upgrade pip
RUN pip install -r requirements.txt
RUN python3 -m spacy download en_core_web_sm

CMD [ "tail", "-f", "/dev/null" ]