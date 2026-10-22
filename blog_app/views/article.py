from blog_app.controllers.article import ArticleController



def article_form(request, article_id: int | None = None):
    return ArticleController(request, article_id).form_page()

def article_delete(request, article_id: int):
    return ArticleController(request, article_id).delete()

def article_view(request, article_id: int):
    return ArticleController(request, article_id).view()

def article_user(request, user_id: int):
    return ArticleController(request).list_by_user(user_id)

def article_category(request, category_id: int):
    return ArticleController(request).list_by_category(category_id)

def article_list(request):
    return ArticleController(request).list()

