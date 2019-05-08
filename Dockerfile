FROM alpine:3.9
WORKDIR /OPT
Copy . /OPT
RUN apk update
RUN apk add --no-cache py-pip
#RUN apk add --update py-pip
RUN apk add build-base libffi-dev python-dev openssl-dev
RUN pip install --upgrade pip
RUN pip install requests
RUN pip install python-telegram-bot
CMD [ "python", "./parser.py" ]
