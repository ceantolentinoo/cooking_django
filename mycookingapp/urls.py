from django.urls import path, include
from . import views

urlpatterns = [
    # ----- RENDER HOME MENU ------ #
    path('', views.index),
    # ----- RENDER CUISINE ------ #
    path('cuisine', views.cuisine),
    # ----- SHOW RECIPES ------ #
    path('<str:category>/<str:type>/recipes/<int:page>', views.recipes),
    # ----- RENDER DIET CATEGORY ------ #
    path('diet', views.diet),
    # ------- RECIPES PREVIOUS PAGE -------- #
    path('prev', views.prev),
    # --------- RENDER SAVED RECIPES --------- #
    path('saved_recipes', views.savedRecipes),
    # --------- USER SAVE RECIPE --------- #
    path('save_recipe', views.saveRecipe),
    # --------- USER SAVE RECIPE --------- #
    path('delete_recipe', views.deleteRecipe),
    # ------- RECIPES NEXT PAGE -------- #
    path('next', views.next),
    # ----- RENDER SHOW RECIPE ------ #
    path('recipe/<int:recipeId>', views.recipe),
    # ------ LOGIN GET & POST --------- #
    path('login', views.login),
    # ------ REGISTER GET & POST --------- #
    path('register', views.register),
    # ------ LOGOUT USER ----------#
    path('logout', views.logout)
]
