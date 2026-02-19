from django.urls import path

from .views import recipe, recipes_list

urlpatterns = [
    path("recipes/list", recipes_list, name="recipes-list"),
    path("recipe/<int:recipe_id>", recipe, name="recipe"),
]

app_name = "ledger"
