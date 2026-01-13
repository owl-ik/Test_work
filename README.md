# Запуск проекта в Docker

1. Запустите контейнеры:
```
docker-compose up -d
```
2. После запуска:
- приложение доступно по адресу: [http://localhost:8000](http://localhost:8000/); aдминка http://localhost:8000/admin/
- для создания админа используем
  ```docker-compose exec web python manage.py createsuperuser```
- для остановки напишите
```
docker-compose down
```
