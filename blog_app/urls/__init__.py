from django.urls import path
from blog_app import views

from .category import category_urls
from .auth import auth_urls
from .article import *
from .reaction import reaction_urls

urlpatterns = [
    *category_urls,
    *auth_urls,
    *article_urls,
    *reaction_urls
]
