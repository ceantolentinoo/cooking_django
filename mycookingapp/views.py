from django.shortcuts import render
import requests

def index(request):
    # url = 'https://api.spoonacular.com/recipes/complexSearch?instructionsRequired=true&apiKey=88aeec238f524b3aafb910b702333739'

    # ####### movie information json ######
    # r = requests.get(url)
    # result = r.json()
    # print(result['results'])
    return render(request, 'index.html')

def cuisine(request):
    return render(request, "cuisine.html")

def diet(request):
    return render(request, "diet.html")

def italian(request):
    # url = 'https://api.spoonacular.com/recipes/complexSearch?instructionsRequired=true&cuisine=italian&addRecipeInformation=true&number=5&apiKey=88aeec238f524b3aafb910b702333739'
    # r = requests.get(url)
    # result = r.json()
    # print(result)
    context = {
        'num': 5,
    }
    return render(request, "italian.html", context)

def recipe(request):
    return render(request, "recipe.html")
