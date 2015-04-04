############################################################
# Dockerfile to build Python WSGI Application Containers
# Based on Ubuntu
############################################################
FROM ubuntu:14.04
MAINTAINER Xu Wang <xuwang@gmail.com>


# Add the application resources URL and install packages
ENV DEBIAN_FRONTEND noninteractive
RUN  apt-get update && apt-get install -yq \
		tar \
		git \
		curl \
		wget \
		nano \
		dialog \
		net-tools \
		build-essential \
		python \
		python-dev \
		python-distribute \
		python-pip \
		libffi-dev \
		libssl-dev
		
# Add application code
ADD /application /application

# Add docker run cmd
ADD /run.sh /run.sh

# Get pip to download and install requirements:
RUN pip install -r /application/requirements.txt

# Expose ports
EXPOSE 80

# Set the default directory where CMD will execute
WORKDIR /application

# Expose /application volume
VOLUME /application

CMD /run.sh