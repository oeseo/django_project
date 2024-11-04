# Django User Management App

Приложение для управления пользователями с использованием Django и Django REST Framework.

## Функционал

- Кастомная модель пользователя с дополнительными полями
- API для получения, редактирования и удаления пользователей
- Токен-авторизация
- Веб-интерфейс для отображения и редактирования пользователей

## Установка

1. Клонируйте репозиторий:
   ```bash
   git clone https://github.com/oeseo/django_project.git

2. Установить зависимости из файла requirements.txt:
   ```bash
   pip install -r requirements.txt

3. Создайте суперпользователя:
   ```bash
   python manage.py createsuperuser

4. Django просканирует ваши модели и создаст миграции для всех приложений:
   ```bash
   python manage.py makemigrations

5. Выполнить миграции:
   ```bash
   python manage.py migrate

6. Запустить проект:
   ```bash
   python manage.py runserver

7. Затем откройте браузер и перейдите на http://127.0.0.1:8000/admin, используя данные суперпользователя

8. Веб-интерфейс для отображения и редактирования пользователей и перейдите на http://127.0.0.1:8000/add-user/#

