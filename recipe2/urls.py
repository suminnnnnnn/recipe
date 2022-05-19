from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('search/', views.SearchFormView.as_view(), name = 'search'),
]