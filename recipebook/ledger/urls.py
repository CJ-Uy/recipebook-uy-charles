from django.urls import path

from .views import recipe, recipes_list, add_recipe

urlpatterns = [
    path("recipes/list", recipes_list, name="recipes-list"),
    path("recipe/<int:recipe_id>", recipe, name="recipe"),
    path("recipe/add", add_recipe, name="add-recipe"),
]

app_name = "ledger"
