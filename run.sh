export ENV=loc                                    # окружение проекта
export PROJECT_NAME=my_shop                            # название проекта
export COMPOSE_PROJECT_NAME=sw-${PROJECT_NAME}      # название проекта в docker
export APP_URL=${PROJECT_NAME}.${ENV}               # урл проекта будет в VIRTUAL_HOST
export COMPOSE_FILE="docker-compose.build.yml"      # указываем какой файл использовать
export COMPOSE_FILE_DEPLOY="docker-compose.${ENV}.swarm.yml" # файл для deploy
export BUILD_NUMBER=latest

#docker-compose -f ${COMPOSE_FILE} config
docker-compose build --force-rm #--no-cache #будет браться указанный файл из переменной окружения

#docker-compose -f ${COMPOSE_FILE_DEPLOY} config
docker stack deploy -c ${COMPOSE_FILE_DEPLOY} ${COMPOSE_PROJECT_NAME} # запуск проекта
#docker-compose -f docker-compose.loc.swarm.yml up