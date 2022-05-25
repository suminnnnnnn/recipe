from argparse import Namespace
from django.urls import path
from . import views

app_name = 'stockapp'

urlpatterns = [
  path('add/', views.add, name='add'),
  path('stock/', views.stock, name='stock'),
  path('stock/delete/<int:stock_id>/', views.delete, name='delete'),
  ]


# from django.urls import path, include
# from .views import StockView, StockDetailView

# app_name = 'stockapp'

# urlpatterns = [
#     path('stock/', StockView.as_view(), name='stock_list'),
#     path('stock/<int:stock_id>/', StockDetailView.as_view(), name='stock_detail')
#     # path('stock/<int:pk>/', stock_detail, name='stock_detail'),
# ]
