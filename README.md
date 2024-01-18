# Ecommerce project for my diploma.

### Развертка сайта:
Для успешного запуска:
- скачать или клонировать репозиторий с github;
- создать .env файл и прописать свой SECRET_KEY для django;
---
### Далее, если вы хотите использовать docker:
- выполнить команду `docker-compose up`;
- запустить миграции `docker-compose run django python manage.py migrate`;
- создать superuser для добавления товаров в магазин `docker-compose run django python manage.py createsuperuser`;
- снова выполнить `docker-compose up` и убедиться, что все работает.
---
#### Развертка по локальной сети:
- создать виртуальную среду и выполнить `pip install -r requirements.txt`;
- у меня в настройках выставлена база данныъ postgresql, при необходимости замените или снимите коммент с sqlite;
- в активном виртуальном окружении выполнить `python manage.py migrate` и далее `python manage.py createsuperuser`;
- выполнить `python manage.py runserver`;
---
## В настоящее время сайт развернут на Timeweb, доступ по ссылке diploma-ecommerce.ru
