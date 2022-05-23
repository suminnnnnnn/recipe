from django.contrib import admin
from django.urls import path
from . import views

app_name='recipe2'
urlpatterns = [
    path('search/', views.SearchFormView.as_view(), name = 'search'),

]