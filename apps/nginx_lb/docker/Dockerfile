FROM nginx:1.9

RUN apt-get update \
	&& apt-get install -y curl \
	&& rm -rf /var/lib/apt/lists/* \
	&& curl -L https://github.com/kelseyhightower/confd/releases/download/v0.9.0/confd-0.9.0-linux-amd64 -o /usr/local/bin/confd \
	&& chmod +x /usr/local/bin/confd \
	&& rm /etc/nginx/conf.d/default.conf
	
ADD ./etc/confd /etc/confd
ADD ./etc/confd-watch /usr/local/bin/confd-watch

RUN chmod +x /usr/local/bin/confd-watch

CMD ["/usr/local/bin/confd-watch"]