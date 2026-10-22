# Инструкция по созданию проекта на Django

#### Шаг 1

Создать проект с uv

---

#### Шаг 2

Установить ```django``` и ```psycopg2```:

```bash
    uv add django psycopg2
```

---

#### Шаг 3

Создаем менеджер приложений:
```bash
    uv run django-admin startproject blog_manager .
```

---

#### Шаг 4

Создаем приложение
```bash
    uv run manage.py startapp blog_app
```

---

#### Шаг 5

Регистрируем приложение в manager:
* В менеджере приложений (```blog_manager```) открыть файл ```settings.py```
* Найти там переменную ```INSTALLED_APPS```
* Добавить в нее первой строкой класс конфига приложения в формате:```<пакет>.<модуль>.<название_класса>```(```'blog_app.apps.BlogAppConfig',```)

---

#### Шаг 6

Запустить сервер:
```bash
    uv run manage.py runserver
```
И убедиться, что на странице ```http://127.0.0.1:8000/``` нет ошибок

---

#### Шаг 7

* Создаем БД в pgAdmin
* В менеджере приложений (```blog_manager```) открыть файл ```settings.py```
* На переменной ```DATABASES``` перейти по ссылке и скопировать пример конфига для PostgreSQL
* Заменить конфиг в ```DATABASES``` и исправить под локальные данные.

---

#### Шаг 8

Применить базовые миграции Django:
```bash
    uv run manage.py migrate
```

---

#### Шаг 9

Создаем суперпользователя:
```bash
    uv run manage.py createsuperuser
```

и следовать его инструкциям

| Во время ввода пароля и его повтора они не отображаются

---

#### Шаг 10

Войти под пользователем из шага 9 на```http://127.0.0.1:8000/admin/```

---

#### Шаг 11

1. В папке с приложением создать папку ```templates```(```blog_app```)
2. В папке с приложением создаем папку ```static```(```blog_app```)
3. В папке ```templates``` создаем ```base.html``` (базовый шаблон) и ```home.html``` (шаблон главной страницы, расширяющий ```base.html```)
4. В папке ```static``` папки ```css``` и ```js```. В них добавить ```index.css``` (базовые стили) и ```index.js```(базовая логика) 

---

#### Шаг 12

1. Создать в папке приложениия пакет ```views```
Добавить в ```__init.py__``` представление для главной страницы (```home.html```):
```python
from django.shortcuts import render

def home_page(request):
    return render(request, "home.html")
```

2. Создать в папке приложения пакет ```urls```. Добавить в ```__init__.py``` маршрут для главной страницы.
```python
from django.urls import path
from blog_app import views

urlpatterns = [
    path("", views.home_page, name="home")
]
```
3. Подключить маршруты приложения в маршруты менеджера приложений
В папке менеджера приложений в ```urls.py``` обавить:
```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("blog_app.urls"))
]
```

---

#### Шаг 13 

Реализовать базовый шаблон (```base.html```) и стили (```index.css```). Расширить базовый шаблон на главной странице(```home.html```)


