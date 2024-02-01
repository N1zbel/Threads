# Django Blog API

Это Django-приложение, предоставляющее API для блогов. Здесь реализованы модели для пользователя, поста и комментария, а также эндпоинты CRUD и пользовательские валидаторы.

## Технологии

- Python 3.8+
- Django 3+
- Django Rest Framework (DRF) 3.10+
- PostgreSQL 10+
- Flake8 для линтинга
- Black и isort для форматирования кода

## Инструкция по Запуску

Для запуска проекта выполните следующие шаги:

1. **Клонирование репозитория:**
   ```bash
   git clone https://github.com/N1zbel/Threads.git
   cd TechTreeNetwork
2. **Создание и активация виртуального окружения:**
    ```bash
   python -m venv venv
   source venv/bin/activate  # Для Windows используйте venv\Scripts\activate
3. **Установка зависимостей:**
    ```bash
   pip install -r requirements.txt
4. **Создайте файл .env в корневой директории проекта и добавьте в него переменные среды, например:**
   * SECRETKEY='КЛЮЧ DJNAGO ПРОЕКТА'
   * DOMAIN_NAME='АДРЕС ДОМЕНА'
   * DB_HOST='ХОСТ БД'
   * POSTGRES_DB='НАЗВАНИЕ БД'
   * POSTGRES_USER='ИМЯ ПОЛЬЗОВАТЕЛЯ БД'
   * POSTGRES_PASSWORD='ПАРОЛЬ ОТ БД'
5. **Настройка базы данных:**
   * Убедитесь, что у вас установлен PostgreSQL и он запущен.
   * Создайте базу данных для проекта через psql или pgAdmin.
   * Убедится что 4-й пункт выполнен (создан и заполнен файл .env)
6. **Применение миграций:**
   ```bash
   python manage.py migrate
7. **Запуск сервера:**
   ```bash
   python manage.py runserver
## Структура проекта

Проект включает три основные модели:

### Пользователь (User)

- **Логин**
- **Пароль**
- **Номер телефона**
- **Дата рождения**
- **Дата создания**
- **Дата обновления**

### Пост (Post)

- **Заголовок**
- **Текст**
- **Изображение (опционально)**
- **Автор (связан с пользователем)**
- **Комментарии**
- **Дата создания**
- **Дата обновления**

### Комментарий (Comment)

- **Автор (связан с пользователем)**
- **Текст**
- **Дата создания**
- **Дата обновления**

## Эндпоинты

### Эндпоинты для пользователя

- **CREATE**: Все пользователи (регистрация).
- **READ**: Администратор/авторизованные пользователи.
- **UPDATE**: Администратор/пользователь может редактировать только себя.
- **DELETE**: Администратор.

### Эндпоинты для постов

- **CREATE**: Авторизованные пользователи.
- **READ**: Все пользователи.
- **UPDATE**: Администратор/пользователь может редактировать только себя.
- **DELETE**: Администратор/пользователь может удалять свои посты.

### Эндпоинты для комментариев

- **CREATE**: Авторизованные пользователи.
- **READ**: Все пользователи.
- **UPDATE**: Администратор/пользователь может редактировать только себя.
- **DELETE**: Администратор/пользователь может удалять свои комментарии.

## Валидаторы

### Модель пользователя (User)

- Валидатор пароля (не менее 8 символов, должен содержать цифры).
- Валидатор электронной почты (разрешены домены: mail.ru, yandex.ru).

### Модель поста (Post)

- Проверка того, что автор поста достиг возраста 18 лет.
- Проверка того, что заголовок не содержит запрещенных слов: ерунда, глупость, чепуха.

## Админ-панель

- Добавлена ссылка на автора в модели поста.
- Добавлен фильтр по дате создания поста.

Для более подробной информации о реализации каждой функции рекомендуется изучить код проекта.
