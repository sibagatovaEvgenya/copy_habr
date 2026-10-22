from django.contrib.auth.models import User
from django.db.models import TextField, Model, ForeignKey, CASCADE

from .article import Article


class Comment(Model):
    content = TextField()
    user = ForeignKey(User, on_delete= CASCADE)
    article = ForeignKey(Article, on_delete=CASCADE)