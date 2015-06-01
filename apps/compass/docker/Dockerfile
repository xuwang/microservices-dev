FROM ubuntu:14.04

ENV HOME /root

RUN apt-get update -qq

# install ruby
RUN apt-get install -y -qq vim-tiny git curl build-essential ruby-dev

# install compass
RUN gem install --no-rdoc --no-ri compass

WORKDIR /srv

ENTRYPOINT ["compass"]
