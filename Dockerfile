FROM ubuntu:18.04

LABEL MAINTAINER="Bleemeo Docker Maintainers <packaging-team@bleemeo.com>"

ADD . /srv/app
RUN apt-get -y update && \
    apt-get -y dist-upgrade && \
    echo LANG=C.UTF-8 >> /etc/environment && \
    apt-get install -y --no-install-recommends python3-pip python3-wheel python3-pkg-resources python3-setuptools python3-dev libmysqlclient-dev gcc libpq-dev && \
    rm -rf /var/lib/apt/lists/* && \
    mkdir -p /srv/app/bleemeo_quote/static && \
    chown -R daemon:daemon /srv/app/bleemeo_quote/static && \
    pip3 install -U pip && \
    pip install --no-cache-dir --upgrade -r /srv/app/requirements.txt

USER daemon
WORKDIR /srv/app
CMD ["/srv/app/deploy/run-uwsgi.sh"]
