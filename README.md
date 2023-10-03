## Запуск backend
- Перейти в директорию: `cd backend`
- Собрать docker контейнер: `docker build -f Dockerfile -t app/backend .`
- Запустить docker контейнер: `docker run --name backend -p 8000:8000 -d --restart always -t app/backend`
- Удалить контейнер: `docker rm -f backend`
- Просмотр логов: `docker logs -f backend`
## Запуск frontend public
- Перейти в директорию: `cd public`
- Собрать docker контейнер: `docker build -t html-server-image:v1 .`
- Запустить docker контейнер: `docker run -d -p 8080:80 html-server-image:v1`
- Удалить контейнер: `docker rm -f frontend`
- Просмотр логов: `docker logs -f frontend`