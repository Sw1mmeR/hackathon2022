# hackathon2022

Для хранения полученных данных со смартфона используем MySQL, ибо хранить всё в .txt не по феншую

Базу данных слоумышленника развернем в контейнере для удобства

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