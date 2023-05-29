# Django проект для получения и редактирования резюме.
Проект используется как микросервис для получения данных о резюме, которые хранятся в базе.
#### Используется:
- Python3;
- Django;
- Swagger;
- Django restf ramework.
## Установка
Используйте в своем виртуальном окружении:
### Заполните файл .env (находится должен рядом с файлом docker-compose.yml):
Пример:
```
DEBUG=False
SECRET_KEY=&f2m8k#y6!@p$=c5ynw!&9ac&o3s&_4=@mp9%uk7vd1oz^+j89
DOMAIN_NAME=http://127.0.0.1

DJANGO_SUPERUSER_USERNAME=admin
DJANGO_SUPERUSER_EMAIL=admin@admin.com
DJANGO_SUPERUSER_PASSWORD=admin

DATABASES_NAME=resume_bd
DATABASES_USER=resume_production
DATABASES_PASSWORD=QWASZX123!
DATABASES_HOST=postgres
DATABASES_PORT=5432

PORT = 8000

```
### Запуск
```
docker-compose up
```
## Использование
- http://127.0.0.1/swagger/ - ссылка на swagger
- http://127.0.0.1/admin/ - ссылка на админку проекта 

## Мок данные
### Пользователи
#### Администратор
login - admin
password - admin

#### Пользователь 
login - test
password - test
* У пользователя test есть одна запись в таблице резюме.

## Авторизация
Авторизация по API происходит с помощью access и refresh токенов, более подробно можно ознакомиться в swagger.
