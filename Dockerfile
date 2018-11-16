FROM alpine:3.8
ENV TOKEN
WORKDIR /OPT
Copy . /OPT
RUN apk add --update py-pip
RUN pip install requests
CMD [ "python", "./parser.py" ]
