from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('menu/', views.index), #views모듈에서 index함수를 가져와라!
    path('menu/<int:pk>/', views.food_detail)
] 