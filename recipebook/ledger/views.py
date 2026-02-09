from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.base import TemplateView

def index(request):
    return render(request, 'index.html')

def recipes_list(request):
    return render(request, 'recipes_list.html')

def recipe_1(request):
    return render(request, 'recipes_1.html')

def recipe_2(request):
    return render(request, 'recipes_2.html')