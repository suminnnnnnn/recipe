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
    stock = Stock(stock_stock=Add_stock, stock_amount=Add_amount,stock_month=Add_month)
    add.save()
    stock.save()

    return render(request, 'stockapp/message.html',{}) 
  return render(request, 'stockapp/add.html', {})

def stock(request):
  stock_list = Stock.objects.all()
  return render(
    request,
    'stockapp/stock.html',
    {'stock_list': stock_list}
  )