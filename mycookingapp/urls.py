from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index),
    path('cuisine', views.cuisine),
    path('diet', views.diet),
    path('italian', views.italian),
]
