from django.db.models import Model, CharField, TextField


class Category(Model):
    name = CharField(max_length=100, unique=True)
    icon = CharField(max_length=20)
    description = TextField(null=True)


    def __str__(self) -> str:
        return self.name
