FROM nginx:stable

MAINTAINER VyacheslavFomenko

RUN apt-get update && apt-get install -y --no-install-recommends curl git

RUN apt-get install -y curl software-properties-common gnupg

RUN curl -sL https://deb.nodesource.com/setup_10.x | bash -
RUN apt-get install -y nodejs build-essential

# установка галпа глобально
RUN npm install gulp-cli -g
COPY ./app/media/package.json /app/media/package.json
WORKDIR /app/media

# установка пакетов из package.json
RUN npm install

# удаляю конфиг с дефолтными настройками
RUN  rm -f /etc/nginx/conf.d/default.conf

# выше всё можно в базовый образ вынести

ARG ENV
EXPOSE 80 443
CMD ["nginx"]

COPY ./docker/nginx/nginx.conf /etc/nginx/
COPY ./docker/nginx/$ENV/nginx-app.conf /etc/nginx/sites-enabled/

COPY ./docker/nginx/run.sh /run.sh
RUN sed -i 's/\r//' /run.sh && chmod +x /run.sh
# gulp отрабатывает потому что запуск происходит из WORKDIR /app/media, где есть gulpfile.js
ENTRYPOINT ["/run.sh"]

COPY ./app /app

COPY ./docker/nginx/$ENV/robots.txt /var/www/project/