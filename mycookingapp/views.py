from django.shortcuts import render, redirect
import requests, math
from django.contrib import messages
from .models import User
import bcrypt

def index(request):
    if 'userLoggedIn' not in request.session:
        return redirect('/login')
    return render(request, 'index.html')

def cuisine(request):
    if 'userLoggedIn' not in request.session:
        return redirect('/login')
    return render(request, "cuisine.html")

def diet(request):
    if 'userLoggedIn' not in request.session:
        return redirect('/login')
    return render(request, "diet.html")

# ------------------SHOW CUISINE RECIPES-----------------------
def recipesCuisine(request,category, type, page):
    if 'userLoggedIn' not in request.session:
        return redirect('/login')
    offset = (page-1) * 10
    if request.method == 'POST':
        del request.session['searchKey']
    if category == 'cuisine':
        url = f'https://api.spoonacular.com/recipes/complexSearch?instructionsRequired=true&offset={offset}&number=10&cuisine={type}&number=5&apiKey=88aeec238f524b3aafb910b702333739'
    elif category == 'diet':
        url = f'https://api.spoonacular.com/recipes/complexSearch?instructionsRequired=true&offset={offset}&number=10&diet={type}&number=5&apiKey=88aeec238f524b3aafb910b702333739'
    elif category == 'search':
        if 'searchKey' not in request.session:
            request.session['searchKey'] = request.POST['search']
        search = request.session['searchKey']
        url = f'https://api.spoonacular.com/recipes/complexSearch?query={search}&offset={offset}&number=10&apiKey=88aeec238f524b3aafb910b702333739'
    else:
         url = f'https://api.spoonacular.com/recipes/complexSearch?instructionsRequired=true&offset={offset}&number=10&type={type}&number=5&apiKey=88aeec238f524b3aafb910b702333739'
    r = requests.get(url)
    print(url)
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
        'category': category,
        'type': type,
        'prevPage': prevPage,
        'nextPage': nextPage,
        'page': page,
        'recipes': recipes,
        'totalPages': math.ceil(result['totalResults']/10)
    }
    return render(request, "recipes.html", context)

# ----------------- RECIPES PREVIOUS PAGE ----------------- #
def prev(request):
    if 'userLoggedIn' not in request.session:
        return redirect('/login')
    page = int(request.POST['currentPage']) - 1
    category = request.POST['category']
    type = request.POST['type']
    return redirect(f'/{category}/{type}/recipes/{page}')

# ----------------- RECIPES NEXT PAGE ----------------- #
def next(request):
    if 'userLoggedIn' not in request.session:
        return redirect('/login')
    page = int(request.POST['currentPage']) + 1
    category = request.POST['category']
    type = request.POST['type']
    return redirect(f'/{category}/{type}/recipes/{page}')

# ------------------SHOW ONE RECIPE-----------------------
def recipe(request, recipeId):
    if 'userLoggedIn' not in request.session:
        return redirect('/login')
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

# ------------------ SHOW & PROCESS LOGIN ---------------------- #
def login(request):
    if 'userLoggedIn' in request.session:
        return redirect('/')
    if request.method == 'POST':
            user = User.objects.filter(email = request.POST['email'])
            if len(user) > 0:
                if bcrypt.checkpw(request.POST['password'].encode(), user[0].password.encode()):
                    print(user[0].__dict__)
                    request.session['userLoggedIn'] = user[0].__dict__['id']
                    return redirect('/')
                else:
                    messages.add_message(request, messages.ERROR,"Invalid email/password!", extra_tags="loginError")
                    return redirect('/login')
            else:
                messages.add_message(request, messages.ERROR,"Invalid email/password!", extra_tags="loginError")
                return redirect('/login')
    return render(request, 'login.html')

# ------------------ LOGOUT --------------------- #
def logout(request):
    del request.session['userLoggedIn']
    return redirect('/login')

# ------------------ SHOW & PROCESS REGISTRATION ---------------------- #
def register(request):
    if 'userLoggedIn' in request.session:
        return redirect('/')
    if request.method == 'POST':
        errors = User.objects.validator(request.POST)
        if len(errors)>0:
            for key, value in errors.items():
                messages.add_message(request, messages.ERROR, value, extra_tags=key)
            return redirect('/register')
        else:
            password = request.POST['password']
            pw_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()

            new_user = User.objects.create(first_name = request.POST['fname'],
            last_name = request.POST['lname'], email = request.POST['email'],
            password=pw_hash)
            messages.add_message(request, messages.INFO,"User created!", extra_tags="userCreated")
            return redirect('/login')
    return render(request, 'register.html')