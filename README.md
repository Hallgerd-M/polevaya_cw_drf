# Трекер для привычек
### Приложение для установления новых полезных привычек

## Описание
Бэкенд-часть SPA-веб приложения по книге Дж.Клира "Атомные привычки". Пользователь регистрируется, указывает полезные и 
приятные привычки, и телеграм-бот присылает ему напоминание о полезной привычке.

## Запуск проекта на сервере

1. Клонируйте репозиторий:
```bash
git clone https://github.com/Hallgerd-M/polevaya_cw_drf.git
cd polevaya_cw_drf
```
 
2. Соберите и запустите контейнеры:
```bash
docker-compose up --build
```
 
3. Примените миграции:
```bash
docker-compose exec web python manage.py migrate
```
 
4. Для создания суперпользователя:
```bash
docker-compose exec web python manage.py createsuperuser
```
 
5. Доступно по адресу: http://localhost:8000

## Запуск проекта локально
1. Клонируйте репозиторий:
```
git clone https://github.com/Hallgerd-M/polevaya_cw_drf
```
2. Установите зависимости:
```
pip install -r requirements.txt
```
3. Создайте базу данных и выполните миграции:
```
python manage.py makemigrations
python manage.py migrate
```
4. Запустите локальный сервер
```
python manage.py runsrver
```
5. Запустите redis

6. Для запуска отложенных задач (отправка сообщений через телеграм-бота) запустите celery и celery beat
```
celery -A config worker -l INFO -P eventlet
celery -A config beat -l INFO 
```
7. Через Postman зарегистрируйте пользователя и привычки

## Документация и структура проекта:
Ознакомиться с моделями и эндпоинтами можно на страницах
[swagger](http://localhost:8000/swagger/) и [redoc](http://localhost:8000/redoc/)

## Контакты
Ирина Полевая / Irina Polevaia
mirwen@yandex.ru

