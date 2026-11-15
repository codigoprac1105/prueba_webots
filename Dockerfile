FROM cyberbotics/webots.cloud:R2025a-ubuntu20.04
ARG PROJECT_PATH=/usr/local/webots-project
RUN mkdir -p $PROJECT_PATH
COPY . $PROJECT_PATH
RUN pip3 install --no-cache-dir paho-mqtt
