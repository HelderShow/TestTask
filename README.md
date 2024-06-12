# TestTask
-- Установка и настройка -- 
1. Клонируйте репозиторий проекта на локальную машину:
* git clone <TestTask>
* cd <test_task>
3. Создайте виртуальное окружение:
* python -m venv env
2. Активируйте виртуальное окружение:
На Windows:
* .\env\Scripts\activate
На macOS/Linux:
* source env/bin/activate
3. Установка зависимостей
Установите все необходимые зависимости:
* pip install -r requirements.txt
4. Настройка базы данных
Примените миграции для настройки базы данных:
* python manage.py makemigrations
* python manage.py migrate

Запуск сервера:
python manage.py runserver
Перейдите в браузере по адресу http://127.0.0.1:8000/

Запрос для создания пользователя-заказчика через API
http://127.0.0.1:8000/api/users/

Запроса для создания задачи
http://127.0.0.1:8000/api/tasks/

Запроса для получения токена:
http://127.0.0.1:8000/api/token/

Запрос с токеном для получения информации о текущем пользователе:
http://127.0.0.1:8000/api/me/

ДОПОЛНИТЕЛЬНО:
Для запуска unit-тестов запустите следующую команду
* python manage.py test
