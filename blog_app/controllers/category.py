from blog_app.forms import CategoryForm
from .base import BaseController
from blog_app.models import Category


class CategoryController(BaseController):
    _CLASS_FORM = CategoryForm
    _REDIRECT_PAGE = "category-list"
    _MODEL = Category
    _ENTITY_NAME = "категорию"
    _ADDITIONAL_JS = [
        "categoryCard"
    ]

    def list(self):
        return super().list_page(
            "category/list.html",
            "Все категории"
        )