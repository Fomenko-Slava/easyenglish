#!/usr/bin/env bash
export ENV=loc                                    # окружение проекта
export PROJECT_NAME=shop                            # название проекта
export COMPOSE_PROJECT_NAME=${PROJECT_NAME}      # название проекта в docker
export APP_URL=${PROJECT_NAME}.${ENV}               # урл проекта будет в VIRTUAL_HOST
export COMPOSE_FILE="docker-compose.build.yml"      # указываем какой файл использовать
export COMPOSE_FILE_DEPLOY="docker-compose.${ENV}.swarm.yml" # файл для deploy
export BUILD_NUMBER=latest
export DJANGO_VIRTUAL_HOST="shop.django.loc"
export DJANGO_VIRTUAL_PORT=8000

#docker-compose build --force-rm #--no-cache
#docker-compose -f ${COMPOSE_FILE_DEPLOY} up
#docker-compose -f ${COMPOSE_FILE_DEPLOY} down

# запуск для разработки
docker-compose -f ${COMPOSE_FILE_DEPLOY} stop shop-django-server &&
    docker-compose -f ${COMPOSE_FILE_DEPLOY} up -d &&
    docker-compose -f ${COMPOSE_FILE_DEPLOY} rm -f shop-django-server &&
    docker-compose -f ${COMPOSE_FILE_DEPLOY} up shop-django-server


#docker-compose -f ${COMPOSE_FILE} config
#docker-compose build --force-rm #--no-cache #будет браться указанный файл из переменной окружения
#docker-compose -f docker-compose.loc.swarm.yml up -d
#docker-compose -f docker-compose.loc.swarm.yml stop


#docker-compose -f ${COMPOSE_FILE_DEPLOY} config
#docker stack deploy -c ${COMPOSE_FILE_DEPLOY} ${COMPOSE_PROJECT_NAME} # запуск проекта

# Удаление
#docker-compose -f docker-compose.loc.swarm.yml down