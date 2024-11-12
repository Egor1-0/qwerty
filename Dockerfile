# Используем официальный образ Python 3.12 как базовый
FROM python:3.12

# Устанавливаем рабочую директорию
WORKDIR /app

# Копируем файл с зависимостями в контейнер
COPY requirements.txt .

# Устанавливаем зависимости
RUN pip install --no-cache-dir -r requirements.txt

# Копируем весь проект в контейнер
COPY . .

# Указываем, что будет запускаться при старте контейнера
CMD ["python", "main.py"]