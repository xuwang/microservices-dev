#FROM dockerhub.stanford.edu/core/ubuntu:20150127-1
FROM ubuntu:vivid
MAINTAINER Xu Wang <xuwang@gmail.com>

# Install base packages
ENV DEBIAN_FRONTEND noninteractive
RUN apt-get update \
    && apt-get -yq install \
        apache2 \ 
		libapache2-mod-auth-mellon \
        curl \
		git
	
# Activate a2enmod
RUN a2enmod rewrite \
	  auth_mellon \
      cgi \
      headers \
      proxy \
      proxy_http \
      proxy_wstunnel \
	  ssl

EXPOSE 80 443
VOLUME /etc/apache2/sites-enabled /etc/apache2/conf-enabled /var/www /usr/lib/cgi-bin /etc/ssl

ADD start.sh /start.sh
RUN chmod 0755 /start.sh
CMD ["bash", "start.sh"]

