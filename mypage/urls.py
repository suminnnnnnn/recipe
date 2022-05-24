from django.shortcuts import render
from django.contrib import admin
from django.urls import path
from . import views

app_name='mypage'
urlpatterns = [
    path('mypage/',views.mypage , name = 'mypage'),
    path('mystock/',views.mystock , name = 'mystock'),

]