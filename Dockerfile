# set base image as Debian Linux OS
FROM debian:stable-slim
# COPY go server to container
COPY docker-bootdev /bin/docker-bootdev
# Start the go server in the container
CMD ["/bin/docker-bootdev"]