FROM debian:buster
RUN echo 'deb http://deb.debian.org/debian buster-backports main' > /etc/apt/sources.list.d/backports.list
RUN apt-get update &&  apt-get install -y \
curl \
python \
wget \
supervisor \
gnupg \
apt-transport-https \
apt-utils \
lsof
RUN curl --silent --location https://raw.githubusercontent.com/micrometreuk/anpr/master/scripts/openalpr-buster.sh | bash -
VOLUME /etc/openalpr/
RUN mkdir -p   /var/lib/openalpr/plateimages
VOLUME /var/lib/openalpr/plateimages
RUN chown 1000:1000 /var/lib/openalpr/plateimages


RUN mkdir -p   /var/log/supervisor
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf
COPY alprd.conf /etc/openalpr/alprd.conf
CMD ["/usr/bin/supervisord"]
WORKDIR ~/
EXPOSE 11300 3000