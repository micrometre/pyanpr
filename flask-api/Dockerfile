FROM python:3-bullseye

RUN echo 'deb http://deb.debian.org/debian buster-backports main' > /etc/apt/sources.list.d/backports.list
RUN apt-get update &&  apt-get install -y \
build-essential \
libssl-dev \
libffi-dev \
python3-dev \
curl \
python3 \
python3-pip \
wget \
supervisor \
gnupg \
apt-transport-https \
apt-utils \
python3-opencv \
inotify-tools \	
lsof
WORKDIR /code
COPY .  /code
RUN pip install -r requirements.txt
RUN curl --silent --location https://raw.githubusercontent.com/micrometreuk/anpr/master/scripts/openalpr-buster.sh | bash -
VOLUME /etc/openalpr/
RUN mkdir -p   /var/lib/openalpr/plateimages
VOLUME /var/lib/openalpr/plateimages
RUN chown 1000:1000 /var/lib/openalpr/plateimages


RUN mkdir -p   /var/log/supervisor
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf
COPY ./config-files/alprd.conf /etc/openalpr/alprd.conf
EXPOSE 5000


CMD python3 --version
CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0", "--debug" ]
