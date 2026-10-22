
from blog_app.models import Category
from .base import BaseForm


class CategoryForm(BaseForm):
    _LABEL_NAME = {
        "name": "Название",
        "icon": "Класс иконки FA",
        "description": "Описание"
    }

    _CUSTOM_CLASS = {
        "icon": "category-icon"
    }

    class Meta:
        model = Category
        fields = "__all__"