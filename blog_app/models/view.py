from django.contrib.auth.models import User
from django.db.models import ForeignKey, SET_NULL, CASCADE, Model

from blog_app.models import Article


class View(Model):
    user = ForeignKey(User, on_delete=SET_NULL, null=True)
    article = ForeignKey(Article, on_delete=CASCADE)