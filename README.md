# 💲 current-usd

Приложение на Django для получения актуального курса доллара к рублю в формате JSON и 10 последних запросов курсов.

---

## Возможности
- Получение актуального курса доллара к рублю

## Используемые технологии

- **Backend:** Django + requests
- **API курса доллара:** [ЦБ РФ](https://www.cbr-xml-daily.ru/)
- **База данных:** SQLite (по умолчанию)

##  Установка

1. **Клонируйте репозиторий:**

```bash
git clone git@github.com:alexsemenovv/current-usd.git
```

2. **Создайте виртуальное окружение при помощи команды**
```bash
python3 -m venv .venv
```
и установите зависимости

```bash
pip install -r requirements.txt
```
3. **Зайдите в корень проекта (mysite)**
- Примените миграции
```bash
python3 manage.py migrate
```

- Запустите приложение
```bash
python3 manage.py runserver
```

- Приложение будет доступно по адресу
```
http://0.0.0.0:8000/
```

## Доступные страницы

| URL      | Описание                                                                           |
|----------|------------------------------------------------------------------------------------|
| `/api/get-current-usd/` | Получение актуального курса доллара к рублю. А также 10 последних запросов курсов. |

## Используемые API
1. Курсы валют ЦБ РФ - получение актуальных котировок доллара к рублю (https://www.cbr-xml-daily.ru/daily_json.js)

##  Структура проекта

```
├── README.md
├── mysite
|   ├── api
|   |   ├── __init__.py
|   |   ├── admin.py
|   |   ├── apps.py
|   |   ├── migrations
|   |   ├── models.py
|   |   ├── tests.py
|   |   ├── urls.py
|   |   └── views.py
|   ├── db.sqlite3
|   ├── manage.py
|   └── mysite
|       ├── __init__.py
|       ├── asgi.py
|       ├── settings.py
|       ├── urls.py
|       └── wsgi.py
└── requirements.txt
```

## Тестирование
Для запуска тестов используйте команду:
```sh
python manage.py test
```

## 🙋‍♂️ Автор
Разработано в рамках тестового задания.
- Контакт: aleksandrsemeonow@yandex.ru
- tg: @alex_semyonov_py