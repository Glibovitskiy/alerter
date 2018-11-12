# use a node base image
FROM alpine:3.8

# set a health check
HEALTHCHECK --interval=5s \
            --timeout=5s \
            CMD curl -f http://127.0.0.1:8000 || exit 1

ENTRYPOINT ["ping", "www.google.com"]

