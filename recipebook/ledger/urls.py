from django.urls import path

from .views import index, recipes_list, recipe_1, recipe_2

urlpatterns = [
    path("", index, name="index"),
    path("list", recipes_list, name="recipes-list"),
    path("1", recipe_1, name="recipe-1"),
    path("2", recipe_2, name="recipe-2"),
]

app_name = "ledger"
