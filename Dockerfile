FROM alpine:3.8
WORKDIR /OPT
Copy . /OPT
RUN apk add --update py-pip
RUN pip install requests
RUN pip py3-telegram-bot
CMD [ "python", "./parser.py" ]
