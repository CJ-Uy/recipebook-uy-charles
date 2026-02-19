from django.shortcuts import render

from ledger.models import Recipe


def index(request):
    return render(request, "index.html")


def recipes_list(request):
    return render(request, "recipes_list.html", {"recipes": Recipe.objects.all()})


def recipe_1(request):
    return render(request, "recipe.html", recipe_1_context)


def recipe_2(request):
    return render(request, "recipe.html", recipe_2_context)
