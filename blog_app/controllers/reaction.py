import json

from django.http import JsonResponse

from .base import BaseController
from blog_app.models import Reaction, Article, Comment


class ReactionController(BaseController):
    _MODEL: Reaction = Reaction

    @classmethod
    def get_article_reactions(cls, article_id: int, current_user: int | None)-> dict:
        article: Article = Article.objects.get(pk=article_id)
        return cls._get_reactions(
            current_user, {"article": article}
        )

    @classmethod
    def get_comment_reactions(cls, comment_id: int, current_user: int | None) -> dict:
        comment: Comment = Comment.objects.get(pk=comment_id)
        return cls._get_reactions(
            current_user, {"comment": comment}

        )

    def set_article_reaction(self, article_id: int, operation: str) -> None:
        article: Article = Article.objects.get(pk=article_id)
        reaction: Reaction= Reaction.objects.filter(
            article=article,
            user=self._request.user
        ).first()
        self._set_reaction(reaction, {"article": article} , operation)


    def set_comment_reaction(self, comment_id: int, operation: str) -> None:
        comment: Comment = Comment.objects.get(pk=comment_id)
        reaction: Reaction = Reaction.objects.filter(
            comment=comment,
            user=self._request.user
        ).first()
        self._set_reaction(reaction, {"comment": comment}, operation)

    def _set_reaction(
        self, reaction: Reaction, params: dict, operation: str
    ) -> None:
        if not reaction:
            new_model = Reaction(
                user=self._request.user,
                is_like=operation == "like",
                **params
            )
            new_model.save()
            return

        if(
            (reaction.is_like and operation == "like")
            or(not reaction.is_like and operation != "like")
        ):
            reaction.delete()
            return

        reaction.is_like = operation == "like"
        reaction.save()


    def change(self)-> JsonResponse:
        body= json.loads(self._request.body)
        entity_type = body.get("entity")
        entity_id = int(body.get("id"))
        operation = body.get("operation")

        getattr(
            self,
            f"set_{entity_type}_reaction"
        )(entity_id, operation)

        return JsonResponse(
            getattr(
                self,
                f"get_{entity_type}_reactions"
            )(entity_id, self._request.user)
        )

    @staticmethod
    def _get_reactions( current_user: int | None, params: dict) -> dict:

        result = {
            "likes": 0,
            "dislikes": 0,
            "is_my_like": False,
            "is_my_dislike": False
        }

        for item in Reaction.objects.filter(**params):
            field: str = "likes" if item.is_like else "dislikes"
            my_field: str = "is_my_like" if item.is_like else "is_my_dislike"

            result[field] += 1

            if current_user and item.user == current_user:
                result[my_field] = True

        return result


