FROM ubuntu:vivid
MAINTAINER Xu Wang <xuwang@gmail.com>

# Install base packages
ENV DEBIAN_FRONTEND noninteractive
RUN apt-get update \
    && apt-get -yq install \
        apache2 \ 
        apache2-dev \ 
        curl \
	git \
        pkg-config \
        build-essential

# Install dependencies for auth_mellon
RUN apt-get -yq install \
    liblasso3 \
    liblasso3-dev \
    libcurl4-openssl-dev

# Build auth_mellon
ENV PKG_VERSION 0.10.0
RUN curl -SL https://github.com/UNINETT/mod_auth_mellon/releases/download/v$PKG_VERSION/mod_auth_mellon-$PKG_VERSION.tar.gz | tar -zxvC /tmp/
RUN cd /tmp/mod_auth_mellon-$PKG_VERSION && ./configure &&  make &&  make install && \
    echo "LoadModule auth_mellon_module /usr/lib/apache2/modules/mod_auth_mellon.so" > /etc/apache2/mods-available/auth_mellon.load
	
# Activate a2enmod
RUN a2enmod rewrite \
    auth_mellon \
    cgi \
    headers \
    include \
    proxy \
    proxy_http \
    proxy_wstunnel \
    ssl
	  
ADD apache2/mellon /etc/apache2/mellon
ADD apache2/ssl /etc/apache2/ssl
ADD start.sh /start.sh
RUN chmod 0755 /start.sh

EXPOSE 80 443

# Expose apache conf, cgi-bin and docroot
VOLUME /etc/apache2/sites-enabled 
VOLUME /etc/apache2/conf-enabled 
VOLUME /etc/apache2/ssl 
VOLUME /etc/apache2/mellon 
VOLUME /usr/lib/cgi-bin 
VOLUME /var/www

CMD ["bash", "start.sh"]

