## Запуск backend
- Перейти в директорию: `cd backend`
- Собрать docker контейнер: `docker build -f Dockerfile -t app/backend .`
- Запустить docker контейнер: `docker run --name backend -p 8000:8000 -d --restart always -t app/backend`
- Удалить контейнер: `docker rm -f backend`
- Просмотр логов: `docker logs -f backend`
## Запуск frontend
- Перейти в директорию: `cd frontend`
- Собрать docker контейнер: `docker build -f Dockerfile -t app/frontend .`
- Запустить docker контейнер: `docker run --name frontend -d -p 8080:80 -d --restart always -t app/frontend`
- Удалить контейнер: `docker rm -f frontend`
- Просмотр логов: `docker logs -f frontend`