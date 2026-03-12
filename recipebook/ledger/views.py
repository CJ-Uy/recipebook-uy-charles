from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from ledger.models import Recipe, Ingredient, RecipeIngredient, Profile, RecipeImage


def index(request):
    return render(request, "index.html")


def recipes_list(request):
    return render(request, "recipes_list.html", {"recipes": Recipe.objects.all()})


@login_required
def recipe(request, recipe_id):
    return render(request, "recipe.html", {"recipe": Recipe.objects.get(pk=recipe_id)})

@login_required
def add_recipe(request):
    allIngredients = Ingredient.objects.all()
    if request.method == "POST":
        newRecipe = Recipe()
        newRecipe.name = request.POST.get("name")
        newRecipe.author = Profile.objects.get(pk=str(request.user.id)) 
        newRecipe.save()
        
        for key, value in request.POST.items():
            if key.startswith("ingredient:") and value != "":
                newRecipeIngredient = RecipeIngredient()
                newRecipeIngredient.ingredient = Ingredient.objects.get(pk=str(key[11:]))
                newRecipeIngredient.recipe = Recipe.objects.get(pk=newRecipe.pk)
                newRecipeIngredient.quantity = value
                newRecipeIngredient.save()
    
    return render(request, "add_recipe.html", {"ingredients": allIngredients})

@login_required
def add_image(request, recipe_id):
    recipeDetails = Recipe.objects.get(pk=recipe_id)
    if request.method == "POST":
        newImage = RecipeImage()
        newImage.recipe = recipeDetails
        newImage.description = request.POST.get("description")
        newImage.image = request.FILES.get("recipeImage")
        newImage.save()
        
        return redirect("/recipes/list")
        
    return render(request, "add_image.html", {"recipe": recipeDetails})