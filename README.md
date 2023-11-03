# api_for_yatube

### Описание
api_for_yatube это готовый API для проекта социальной сети блогеров Yatube. Он предназначен для взаимодействия приложений клиента с бэкендом проекта Yatube через JSON формат. Позволяет регистрироваться на сайте, создавать и редактировать посты, подписываться на понравившихся авторов и добавляться в различные сообщества.
### Технологии
***язык программирования***
- Python 3.7
***зависимости***

- Django==3.2.16
- pytest==6.2.4
- pytest-pythonpath==0.7.3
- pytest-django==4.4.0
- djangorestframework==3.12.4
- djangorestframework-simplejwt==4.7.2
- Pillow==9.3.0
- PyJWT==2.1.0
- requests==2.26.0
- djoser==2.1.0


### Как запустить проект:

- Клонировать репозиторий и перейти в него в командной строке:

```
git clone https://github.com/AlDrPy/api_for_yatube
```

```
cd api_for_yatube/
```

- Cоздать виртуальное окружение:

```python -m venv venv``` или ```python3 -m venv venv```
и затем активировать его:
```source venv/Scripts/activate``` для Windows
либо ```source venv/bin/activate``` для Linux

- Установить зависимости из файла requirements.txt:

```
python -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```

- Перейти в директорию с файлом manage.py ```cd yatube_api/```
  и выполнить миграции:

```
python manage.py migrate
```

- Запустить проект на локальной машине:

```
python manage.py runserver
```
- Готово! Теперь можно подключить своё приложение или протестировать работу API с помощью Postman.

Браузерный интерфейс API будет доступен по адресу http://127.0.0.1:8000/api/v1/
Документация размещена по адресу http://127.0.0.1:8000/redoc/

### Авторы
_AlDrPy  https://github.com/AlDrPy_
