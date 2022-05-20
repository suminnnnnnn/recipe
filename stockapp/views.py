from ast import Add
from django.http import HttpResponse
from django.shortcuts import render
from .models import Add

def add(request):
  if request.method == 'POST':
    Add_stock = request.POST.get('Add_stock')
    Add_amount = request.POST.get('Add_amount')
    Add_month = request.POST.get('Add_month')
  
    
    add = Add(Add_stock=Add_stock, Add_amount=Add_amount,Add_month=Add_month)
    add.save()

    return HttpResponse('재료 등록 완료') 
  return render(request, 'stockapp/add.html', {})
