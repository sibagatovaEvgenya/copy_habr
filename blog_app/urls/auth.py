from django.urls import path

from blog_app.views import login_page, register_page, logout_page

auth_urls = [
    path("login/", login_page, name="login"),
    path("register/", register_page, name="register"),
    path("logout/", logout_page, name="logout")
]
