from django.urls import path
from . import views

app_name = 'stockapp'

urlpatterns = [
  path('add/', views.add),
  path('stock/', views.stock, name='stock'),
]