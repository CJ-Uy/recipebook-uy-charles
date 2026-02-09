from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.base import TemplateView

recipes_list_context = {
    "recipes": [
        {
            "name": "Recipe 1",
            "ingredients": [
                {
                    "name": "tomato",
                    "quantity": "3pcs"
                },
                {
                    "name": "onion",
                    "quantity": "1pc"
                },
                {
                    "name": "pork",
                    "quantity": "1kg"
                },
                {
                    "name": "water",
                    "quantity": "1L"
                },
                {
                    "name": "sinigang mix",
                    "quantity": "1 packet"
                }
            ],
            "link": "/recipe/1"
        },
        {
            "name": "Recipe 2",
            "ingredients": [
                {
                    "name": "garlic",
                    "quantity": "1 head"
                },
                {
                    "name": "onion",
                    "quantity": "1pc"
                },
                {
                    "name": "vinegar",
                    "quantity": "1/2cup"
                },
                {
                    "name": "water",
                    "quantity": "1 cup"
                },
                {
                    "name": "salt",
                    "quantity": "1 tablespoon"
                },
                {
                    "name": "whole black peppers",
                    "quantity": "1 tablespoon"
                },
                {
                    "name": "pork",
                    "quantity": "1 kilo"
                }
            ],
            "link": "/recipe/2"
        }
    ]
}

recipe_1_context = {
	"name": "Recipe 1",
	"ingredients": [
		{
			"name": "tomato",
			"quantity": "3pcs"
		},
		{
			"name": "onion",
			"quantity": "1pc"
		},
		{
			"name": "pork",
			"quantity": "1kg"
		},
		{
			"name": "water",
			"quantity": "1L"
		},
		{
			"name": "sinigang mix",
			"quantity": "1 packet"
		}
	],
	"link": "/recipe/1"
}


recipe_2_context = {
    "name": "Recipe 2",
    "ingredients": [
        {
            "name": "garlic",
            "quantity": "1 head"
        },
        {
            "name": "onion",
            "quantity": "1pc"
        },
        {
            "name": "vinegar",
            "quantity": "1/2cup"
        },
        {
            "name": "water",
            "quantity": "1 cup"
        },
        {
            "name": "salt",
            "quantity": "1 tablespoon"
        },
        {
            "name": "whole black peppers",
            "quantity": "1 tablespoon"
        },
        {
            "name": "pork",
            "quantity": "1 kilo"
        }
    ],
    "link": "/recipe/2"
}


def index(request):
    return render(request, 'index.html')

def recipes_list(request):
    return render(request, 'recipes_list.html', recipes_list_context)

def recipe_1(request):
    return render(request, 'recipes_1.html', recipe_1_context)

def recipe_2(request):
    return render(request, 'recipes_2.html', recipe_2_context)