# hackathon2022

Для хранения полученных данных со смартфона используем MySQL, ибо хранить всё в .txt не по феншую

Базу данных злоумышленника развернем в контейнере для удобства

Для создания контейнера:

> Создаем сеть для взаимодействия с контейнером
```
docker network create intruder_net
```
> Загружаем image с установленным mysql, пробрасываем порт 3306, для взаимодействия с нашей машиной.
> Указываем нашу сетку intruder_net.
> Создаем БД hacker_db в контейнере.
```
docker run --name=mysql -p 3306:3306 --network=intruder_net  -e MYSQL_ROOT_HOST=%
-e MYSQL_ROOT_PASSWORD=root -e MYSQL_DATABASE=hacker_db -d mysql:latest
```
> Чтобы зайти в контейнер делаем docker ps, копируем DOCKER ID
```
docker ps
CONTAINER ID   IMAGE          COMMAND                  CREATED         STATUS         PORTS                               NAMES
9e6f50f6d3c9   mysql:latest   "docker-entrypoint.s…"   4 minutes ago   Up 4 minutes   0.0.0.0:3306->3306/tcp, 33060/tcp   mysql
```
> Чтобы войти в контейнер по ID
```
docker exec -ti 9e6f50f6d3c9 /bin/bash
```