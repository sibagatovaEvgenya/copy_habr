from blog_app.controllers.reaction import ReactionController
from blog_app.models import Reaction


def change_reaction(request):
    return ReactionController(request).change()
