# Базовый образ
FROM python:3.9

# Установка зависимостей
WORKDIR /app
COPY requirements .
RUN pip install -r requirements/base.txt

# Копирование исходного кода проекта
COPY . .

# Порт, на котором работает ваше приложение
EXPOSE 8000

# Запуск команды для запуска приложения
CMD ["python", "manage.py", "makemigrations"]
CMD ["python", "manage.py", "migrate"]
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
