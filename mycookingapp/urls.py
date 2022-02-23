from django.urls import path, include
from . import views

urlpatterns = [
    # ----- RENDER HOME MENU ------ #
    path('', views.index),
    # ----- RENDER CUISINE ------ #
    path('cuisine', views.cuisine),
    # ----- RENDER ITALIAN ------ #
    path('cuisine/<str:cuisine>/recipes/<int:page>', views.recipesCuisine),
    # ----- RENDER DIET CATEGORY ------ #
    path('diet', views.diet),
    # ------- RECIPES PREVIOUS PAGE -------- #
    path('prev', views.prev),
    # ------- RECIPES NEXT PAGE -------- #
    path('next', views.next),
    # ----- RENDER SHOW RECIPE ------ #
    path('recipe/<int:recipeId>', views.recipe)
]
