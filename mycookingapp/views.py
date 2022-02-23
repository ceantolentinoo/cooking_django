from django.shortcuts import render, redirect
import requests, math

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

# ------------------SHOW CUISINE RECIPES-----------------------
def recipesCuisine(request, cuisine, page):
    offset = (page-1) * 10
    url = f'https://api.spoonacular.com/recipes/complexSearch?instructionsRequired=true&offset={offset}&number=10&cuisine={cuisine}&number=5&apiKey=88aeec238f524b3aafb910b702333739'
    r = requests.get(url)
    result = r.json()
    recipes = result['results']
    if result['offset'] == 0:
        prevPage = False
    else:
        prevPage = True

    if page+1 <= math.ceil(result['totalResults']/10):
        nextPage = True
    else:
        nextPage = False
    context = {
        'num': 5,
        'cuisine': cuisine,
        'prevPage': prevPage,
        'nextPage': nextPage,
        'page': page,
        'recipes': recipes,
        'totalPages': math.ceil(result['totalResults']/10)
    }
    return render(request, "recipes.html", context)

# ----------------- RECIPES PREVIOUS PAGE ----------------- #
def prev(request):
    page = int(request.POST['currentPage']) - 1
    cuisine = request.POST['type']
    return redirect(f'/recipes/{cuisine}/{page}')

# ----------------- RECIPES NEXT PAGE ----------------- #
def next(request):
    page = int(request.POST['currentPage']) + 1
    cuisine = request.POST['type']
    return redirect(f'/recipes/{cuisine}/{page}')

# ------------------SHOW ONE RECIPE-----------------------
def recipe(request, recipeId):
    url = f'https://api.spoonacular.com/recipes/{recipeId}/information?apiKey=88aeec238f524b3aafb910b702333739'
    r = requests.get(url)
    recipe = r.json()
    context = {
        'title': recipe['title'],
        'recipeImg': recipe['image'],
        'summary': recipe['summary'],
        'readyInMinutes': recipe['readyInMinutes'],
        'rating': recipe['aggregateLikes'],
        'vegetarian': recipe['vegetarian'],
        'vegan': recipe['vegan'],
        'glutenFree': recipe['glutenFree'],
        'dairyFree': recipe['dairyFree'],
        'ingredients': recipe['extendedIngredients'],
        'instructions': recipe['analyzedInstructions'][0]['steps']
    
    }
    return render(request, "recipe.html", context)
