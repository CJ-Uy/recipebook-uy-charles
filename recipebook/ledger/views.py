from django.shortcuts import render

from ledger.models import Recipe


def index(request):
    return render(request, "index.html")


def recipes_list(request):
    return render(request, "recipes_list.html", {"recipes": Recipe.objects.all()})


def recipe(request, recipe_id):
    return render(request, "recipe.html", {"recipe": Recipe.objects.get(pk=recipe_id)})
