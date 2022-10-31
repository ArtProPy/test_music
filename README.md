# test_music
Тестовый микросервис

### Предусловия для корректной работы микросервиса

* Должен быть установлен python3.7 глобально.
* Должна быть запущена PostgreSQL с созданной базой данных, имя которой соответствует
имени в конфигурации (файл .env).


### Установка
#### Как развернуть проект для разработки:

1. Склонируйте проект
```bash
    git clone https://github.com/ArtProPy/organizations.git
```

2. Создайте и активируйте виртуальное окружение 

3. Установите poetry
```bash
    pip install poetry
```

4. Установите зависимости проекта
```bash
  poetry install
```

5. Создайте файл `.env` на основе шаблона `.env.template`

6. Накатите миграции:
```bash
  .../venv/bin/django-admin migrate
```

7. Запустите сервер
```bash
  .../venv/bin/django-admin runserver