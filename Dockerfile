# Используем базовый образ Python
FROM python:3.10

# Копируем зависимости проекта
COPY requirements.txt .

# Устанавливаем зависимости
RUN pip install -r requirements.txt

EXPOSE 5432

# Копируем все файлы проекта в контейнер
COPY . /app/

# Устанавливаем рабочую директорию внутри контейнера
WORKDIR app

# Определяем переменные среды
ENV PYTHONUNBUFFERED=1

# Запускаем команду для запуска приложения
#CMD ["python", "manage.py", "runserver"]
