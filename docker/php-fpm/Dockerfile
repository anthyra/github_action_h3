FROM php:8.0-fpm-buster

RUN apt-get update && \
    apt-get install -y --no-install-recommends git

RUN apt-get update

WORKDIR /var/www/html

CMD php-fpm

EXPOSE 9000