FROM alpine:3.6
WORKDIR /OPT
Copy . /OPT
RUN apk add --update py-pip
RUN pip install requests
CMD [ "python", "./parser.py" ]
