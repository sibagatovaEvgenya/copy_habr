from django.urls import path
from blog_app import views

category_urls = [
    path(
        "category/list/",
        views.category_list,
        name="category-list"
    ),
    path(
        "category/add/",
        views.category_form,
        name="category-add"
    ),
    path(
        "category/update/<int:category_id>/",
        views.category_form,
        name="category-update"
    ),
    path(
        "category/delete/<int:category_id>/",
        views.category_delete,
        name="category-delete"
    )
]
