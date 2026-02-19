from django.urls import path

from .views import index, recipe, recipes_list

urlpatterns = [
    path("", index, name="index"),
    path("recipes/ist", recipes_list, name="recipes-list"),
    path("recipe/<int:recipe_id>", recipe, name="recipe"),
]

app_name = "ledger"
