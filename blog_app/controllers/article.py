from django.contrib.auth.models import User
from django.forms.models import model_to_dict
from django.shortcuts import render

from blog_app.forms import ArticleForm
from .base import BaseController
from blog_app.models import Article, Category, Comment, View
from .reaction import ReactionController


class ArticleController(BaseController):
    _CLASS_FORM = ArticleForm
    _REDIRECT_PAGE = "home"
    _MODEL = Article
    _ENTITY_NAME = "статью"

    def list(self, models = None):
        return super().list_page(
            "article/list.html",
            "Главная",
            models
        )

    def list_by_user(self, user_id: int):
        user = User.objects.get(pk=user_id)
        models = []

        if user:
            models = Article.objects.filter(user=user) or []

        return self.list(models)

    def list_by_category(self, category_id: int):
        category = Category.objects.get(pk=category_id)
        models = []

        if category:
            models = Article.objects.filter(
                category=category
            ) or []

        return self.list(models)

    def view(self):
        article: Article = Article.objects.get(pk=self._entity_id)

        if (self._is_post
            and (comment := self._request.POST.get("content"))
        ):
                new_model: Comment = Comment(
                    content=comment,
                    article=article,
                    user=self._request.user
                )

                new_model.save()
        else:
            self._add_view()




        return render(
            self._request,
            'article/view.html',
            {
                "article": article,
                **self._get_extra_article_data(article)
            }
        )


    def _before_form_save(self, form: ArticleForm):
        form.instance.user = self._request.user

    def _has_access(self):
        return (
            self._request.user
            and self._entity_id
            and (entity := self._MODEL.objects.get(pk=self._entity_id))
            and self._request.user.id == entity.user.id

        )

    def _get_extra_article_data(self, article: Article) -> dict:
        comments: list[Comment] = Comment.objects.filter(article=article).order_by("-id") or []
        views_count: int = len(View.objects.filter(article=article) or [])

        comments_dict: list[dict] = [
            {
                **model_to_dict(comment),
                "user": model_to_dict(comment.user),
                "reaction": ReactionController.get_comment_reactions(
                    comment.pk,
                    self._request.user
                )
            } for comment in comments
        ]


        return {
            "comments": comments_dict,
            "comments_count": len(comments),
            "views_count": views_count,
            "reaction": ReactionController.get_article_reactions(self._entity_id, self._request.user ),
            "popular_articles": self.get_popular_article()
        }
    def _add_view(self) -> None:
        if self._request.user.id:
            article = Article.objects.get(pk=self._entity_id)
            exist_view = View.objects.filter(
                user=self._request.user,
                article=article
            )

            if not exist_view:
                new_view = View(
                    article=article,
                    user=self._request.user
                )
                new_view.save()

        else:
            viewing_article_str: str = self._request.COOKIES.get("viewing_article") or ""
            viewing_articles: list[int] = list(map(int, viewing_article_str.split(","))) if viewing_article_str else []

            if self._entity_id not in viewing_articles:
                article = Article.objects.get(pk=self._entity_id)
                new_view = View(
                    article=article,
                )
                new_view.save()






