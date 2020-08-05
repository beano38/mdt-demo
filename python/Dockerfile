FROM python:3-alpine

RUN apk update \
    && apk --no-cache --update add build-base

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . /usr/src/app

EXPOSE 9998

CMD [ "python", "-u", "./snmpapi.py" ]
