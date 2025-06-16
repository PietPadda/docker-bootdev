# set base image as Debian Linux OS
FROM debian:stable-slim
# COPY go server to container
COPY docker-bootdev /bin/docker-bootdev
# Set port via OS env
ENV PORT=8991
# Start the go server in the container
CMD ["/bin/docker-bootdev"]