# Base image.
ARG BASE_IMAGE

FROM $BASE_IMAGE

# Override user name and user id at build.
ARG DOCKER_USER
ARG DOCKER_USER_ID

# Create a group and user
RUN adduser --uid $DOCKER_USER_ID --disabled-password $DOCKER_USER
