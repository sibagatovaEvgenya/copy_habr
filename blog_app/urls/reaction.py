from blog_app.views import change_reaction
from django.urls import path

reaction_urls = [
    path("reaction/change",
    change_reaction,
    name="change-reaction"
    )
]