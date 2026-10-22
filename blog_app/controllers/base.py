from functools import cached_property

from django.db.models import Model
from django.forms import Form, ModelForm
from django.http import HttpRequest
from django.shortcuts import render, redirect

from blog_app.models import Article


class BaseController:
    _CLASS_FORM: type[ModelForm]
    _REDIRECT_PAGE: str = ""
    _MODEL: type[Model] | None = None
    _ENTITY_NAME: str
    _ADDITIONAL_JS: list[str] = []

    def __init__(self, request: HttpRequest , entity_id: int | None = None) -> None:
        self._request: HttpRequest = request
        self._is_post: bool = request.method == "POST"
        self._entity_id: int | None = entity_id

    @cached_property
    def model(self) -> Model | None:
        if not self._MODEL or not self._entity_id:
            return None

        try:
            return self._MODEL.objects.get(pk=self._entity_id)
        except Exception:
            return None

    @cached_property
    def form(self) -> ModelForm | None:
        if self._is_post:
            if self.model:
                return self._CLASS_FORM(self._request.POST, instance=self.model)

            form = self._CLASS_FORM(self._request.POST)
            self._before_form_save(form)
            return form


        if self.model:
            return self._CLASS_FORM(instance=self.model)

        if self._entity_id:
            return None

        return self._CLASS_FORM()

    def form_page(self):
        if not self._has_access():
            return redirect(self._REDIRECT_PAGE)

        if self._is_form_submitted():
            return redirect(self._REDIRECT_PAGE)

        return self._render_form_page()

    def delete(self):
        if not self._has_access():
            return redirect(self._REDIRECT_PAGE)

        if self.model:
            self.model.delete()

        return redirect(self._REDIRECT_PAGE)

    def list_page(self, template: str, title: str, models = None):
        return render(
            self._request,
            template,
            {
                "title": title,
                "entities": (
                    models
                    if models is not None
                    else self._MODEL.objects.all()
                ),
                "popular_articles": self.get_popular_article()
    })


    def _is_form_submitted(self) -> bool:
        if not self._is_post or not self.form.is_valid():
            return False

        return self._form_submit()

    def _form_submit(self) -> bool:
        self.form.save()

        return True

    def _render_form_page(self):
        if not self.form:
            return redirect(self._REDIRECT_PAGE)

        return render(
            self._request,
            "form.html",
            self._get_form_page_context()
        )

    def _get_form_page_context(self) -> dict:
        action_prefix: str = "Добавить" if not self._entity_id else "Изменить"

        return {
            "form": self.form,
            "title": f"{action_prefix} {self._ENTITY_NAME}",
            "page_title": f"{action_prefix} {self._ENTITY_NAME}",
            "btn_text": action_prefix,
            "additional_js": self._ADDITIONAL_JS
        }

    def _before_form_save(self, form):
        ...

    def _has_access(self):
        return True

    @staticmethod
    def get_popular_article():
        return Article.objects.raw("""
        WITH likes_count AS (
            SELECT 
                A."id",
                COUNT(R."id") AS "Count"

            FROM 
                "blog_app_article" AS A
                LEFT JOIN "blog_app_reaction" AS R
                    ON R."article_id" = A."id"
                        AND R."is_like" IS TRUE

            GROUP BY
                A."id"

        ),
        dislikes_count AS(
            SELECT 
                A."id",
                COUNT(R."id") AS "Count"

            FROM 
                "blog_app_article" AS A
                LEFT JOIN "blog_app_reaction" AS R
                    ON R."article_id" = A."id"
                        AND R."is_like" IS FALSE

            GROUP BY
                A."id"

        ),
        comments_count AS (
            SELECT 
                A."id",
                COUNT(C."id") AS "Count"

            FROM 
                "blog_app_article" AS A
                LEFT JOIN "blog_app_comment" AS C
                    ON C."article_id" = A."id"

            GROUP BY
                A."id"

        ),

        views_count AS (
            SELECT 
                A."id",
                COUNT(V."id") AS "Count"

            FROM 
                "blog_app_article" AS A
                LEFT JOIN "blog_app_view" AS V
                    ON V."article_id" = A."id"

            GROUP BY
                A."id"

        )

        SELECT 
            A."id",
            A."title"

        FROM
            "blog_app_article" AS A
            JOIN likes_count AS LC
                USING("id")
            JOIN dislikes_count AS DC
                USING("id")
            JOIN comments_count AS CC
                USING("id")
            JOIN viewS_count AS VC
                USING("id")

        ORDER BY
            (
                LC."Count" * 100
                + DC."Count" * 50
                + CC."Count" * 5
                + VC."Count" * 0.5

            ) DESC

        LIMIT
            5       


        """)
