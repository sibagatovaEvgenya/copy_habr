from django.contrib.auth.models import User
from django.db.models import Model, ForeignKey, CASCADE, CharField, TextField

from .category import Category


class Article(Model):
    title = CharField(max_length=100)
    content = TextField()
    image = CharField(max_length=100)

    category = ForeignKey(Category, on_delete=CASCADE)
    user = ForeignKey(User, on_delete=CASCADE)

    @property
    def limit_content(self) -> str:
        if len(self.content) <= 250:
            return self.content
        return self.content[:250] + "..."



    @property
    def formated_content(self) -> str:
        return self.content.replace("\n", "<br>")








def __str__(self) -> str:
    return self.title

