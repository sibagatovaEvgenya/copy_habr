from django.urls import path
from blog_app import views

article_urls = [
    path( 
        "", views.article_list, name="home"
        ),
    path(
        "article/add/",
        views.article_form,
        name="article-add"
    ),
    path(
        "article/update/<int:article_id>/",
        views.article_form,
        name="article-update"
    ),
    path(
        "article/delete/<int:article_id>/",
        views.article_delete,
        name="article-delete"
    ),
    path(
        "article/<int:article_id>",
        views.article_view,
        name="article-view"
    ),
    path(
        "article/user/<int:user_id>",
        views.article_user,
        name="article-user"
    ),
    path(
        "article/category/<int:category_id>",
        views.article_category,
        name="article-category"
    ),
]
