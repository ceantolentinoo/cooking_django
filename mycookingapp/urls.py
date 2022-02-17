from django.urls import path, include
from . import views

urlpatterns = [
    # ----- RENDER HOME MENU ------ #
    path('', views.index),
    # ----- RENDER CUISINE ------ #
    path('cuisine', views.cuisine),
    # ----- RENDER DIET CATEGORY ------ #
    path('diet', views.diet),
    # ----- RENDER ITALIAN ------ #
    path('italian', views.italian),
    # ----- RENDER SHOW RECIPE ------ #
    path('recipe', views.recipe)
]
