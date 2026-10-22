from django.shortcuts import render

from blog_app.controllers import CategoryController
from blog_app.models import Category


def category_list(request):
    return CategoryController(request).list()


def category_form(request, category_id: int | None = None):
    return CategoryController(request, category_id).form_page()

def category_delete(request, category_id: int):
    return CategoryController(request, category_id).delete()