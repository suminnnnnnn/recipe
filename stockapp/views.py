from ast import Add
from django.http import HttpResponse
from django.shortcuts import render
from .models import Add

def add(request):
  if request.method == 'POST':
    stock = request.POST.get('stock')
    amount = request.POST.get('amount')
  
    
    add = Add(stock=stock)
    #amount = Add(amount=amount)
    add.save()
    #amount.save()

    return HttpResponse('재료 등록 완료')
  return render(request, 'stockapp/add.html', {})
