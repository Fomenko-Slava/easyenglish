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

RUN npm install

#COPY ./app/media/package.json /app/media/package.json
#RUN cd /app/media/ && npm install

# удаляю конфиг с дефолтными настройками
RUN  rm -f /etc/nginx/conf.d/default.conf

# выше всё можно в базовый образ вынести

ARG ENV

COPY ./app /app

# это только для локалки актуально
#RUN rm -rf /var/www/project/media/node_modules/

# копируем node_modules, которые установлены в базовом образе
#RUN mv /tmp/node_modules /var/www/project/media

COPY ./docker/nginx/nginx.conf /etc/nginx/
COPY ./docker/nginx/$ENV/nginx-app.conf /etc/nginx/sites-enabled/
COPY ./docker/nginx/$ENV/robots.txt /var/www/project/

CMD ["nginx"]

#COPY ./docker/nginx/run.sh /run.sh

#RUN sed -i 's/\r//' /run.sh \
#    && chmod +x /run.sh

RUN nohup gulp

#ENTRYPOINT ["/run.sh"]

EXPOSE 80 443