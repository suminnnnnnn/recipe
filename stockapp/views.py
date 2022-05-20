from ast import Add
from django.http import HttpResponse
from django.shortcuts import render
from .models import Add ,Stock

def add(request):
  if request.method == 'POST':
    Add_stock = request.POST.get('Add_stock')
    Add_amount = request.POST.get('Add_amount')
    Add_month = request.POST.get('Add_month')
  
    
    add = Add(Add_stock=Add_stock, Add_amount=Add_amount,Add_month=Add_month)
    add.save()

    return render(request, 'stockapp/message.html',{}) 
  return render(request, 'stockapp/add.html', {})

def stock(request):
  if request.method == 'GET':
    stock_name = request.GET.get('Add_stock')
    stock_amount = request.GET.get('Add_amount')
    stock_month = request.GET.get('Add_month')

  return render(request, 'stockapp/stock.html')
