Перед початком роботи переконайтеся, що встановлені наступні компоненти:

- Python 3.x
- Фреймворк django
- Бібліотека mongoengine
- Бібліотека pymongo
- Бібліотека psycopg2
- Бібліотека django-environ

## Встановлення та налаштування

1. Склонуйте репозиторій проекту на свій локальний комп'ютер.
2. Встановіть необхідні залежності
3. В каталозі проекту створіть файл .env та додайте туди свої дані за таким шаблоном:
SECRET_KEY=

DATABASE_NAME= 
DATABASE_USER= 
DATABASE_PASSWORD= 
DATABASE_HOST= 
DATABASE_PORT=

EMAIL_HOST= 
EMAIL_PORT= 
EMAIL_HOST_USER= 
EMAIL_HOST_PASSWORD=

4. Створіть підключення до бази даних Postgres
5. Для запуску серверу виконайте команду python manage.py runserver 
6. Після запуску серверу веб-застосунок буде доступним за посиланням http://localhost:8000/ 
