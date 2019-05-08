FROM alpine:3.8
WORKDIR /OPT
# RUN apk add --no-cache py-pip
RUN apk add --update py-setuptools
RUN apk add build-base libffi-dev python-dev openssl-dev
RUN pip install --upgrade pip
RUN pip install requests
RUN pip install python-telegram-bot
CMD [ "python", "./parser.py" ]
