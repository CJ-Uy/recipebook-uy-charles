from django.db import models
from django.urls import reverse


class Ingredient(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("view-name", args=[str(self.name)])


class Recipe(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("view-name", args=[self.pk])


class RecipeIngredient(models.Model):
    quantity = models.CharField(255)
    ingredient = models.ForeignKey(
        Ingredient, on_delete=models.CASCADE, related_name="recipe"
    )
    recipe = models.ForeignKey(
        Recipe, on_delete=models.CASCADE, related_name="ingredients"
    )

    def __str__(self):
        return f"{self.recipe.name} : {self.ingredient.name} : {self.quantity}"
