from django.contrib import admin
from django.urls import path
from calorie import views

urlpatterns = [
    path('',views.main,name='main'),
]