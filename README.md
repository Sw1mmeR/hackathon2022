# hackathon2022

Для хранения полученных данных со смартфона используем MySQL, ибо хранить всё в .txt не по феншую

Базу данных злоумышленника развернем в контейнере для удобства

**Для импорта контейнера:**
=
```
docker load -i mysql_hack.tar
```
**Для создания контейнера:**
=
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
> Чтобы войти в контейнер по ID (Если идете просто по гайду, то заходить в контейнер не нужно, подключимся из нашей системы сразу к MySQL)
```
docker exec -ti 9e6f50f6d3c9 /bin/bash
```
> Скачиваем клиент mysql, если такового не имеется, ссылка для шиндовс:
`https://dev.mysql.com/downloads/mysql/`

>Разархивируем куда-нибудь и прописываем путь к папке bin в PATH
```
set PATH=%PATH%;"C:\mysql-8.0.31-winx64\bin"
```
>Подключаемся к MySQL
```
mysql -h localhost -u root -p
```
> Создаем таблицу target_phone с полями name и number
```
use hacker_db;
CREATE TABLE target_phone (name VARCHAR(20), number VARCHAR(11));
```
> Вставляем тестовую запись в БД
```
INSERT INTO target_phone (name, number) VALUES ('Test', '79139445566');
```
> Проверяем
```
SELECT * FROM target_phone;

Ожидаемый вывод:
+------+-------------+
| name | number      |
+------+-------------+
| Test | 79139445566 |
+------+-------------+
1 row in set (0.00 sec)
```
> Всё ок, теперь можно из скрипта делать записи в БД

**Как поднять сервер злоумышленника**
=
> Переходим в директорию с docker-compose.yml и делаем build
```
docker-compose build
```
> Когда всё успешно забилдилось  делаем
```
docker-compose up
```
> У нас успешно поднялся контейнер, в котором запущен скрипт server.py (он всё также будет писать данные в БД, развернутой в первом контейнере)