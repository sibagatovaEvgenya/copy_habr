from blog_app.models import Article
from .base import BaseForm



class ArticleForm(BaseForm):
    _LABEL_NAME = {
        "title": "Заголовок",
        "content": "Содержимое",
        "image": "Картинка",
        "category": "Категория"
    }


    class Meta:
        model = Article
        fields = [
            "title",
            "content",
            "image",
            "category"
        ]