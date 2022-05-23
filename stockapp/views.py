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
   
    stock_stock = request.GET.get('Add.Add_stock')
    stock_amount = request.GET.get('Add.Add_amount')
    stock_month = request.GET.get('Add.Add_month')
    Adds = Add.objects.all()
    print(Adds)
  
  
    # Stock = Stock(stock_stock=stock_stock, stock_amount=stock_amount, stock_month=stock_month)

    return render(request, 'stockapp/stock.html')

# def stock(request):
#   # jeju_olle_list = JejuOlle.objects.all()
#   # print(jeju_olle_list)

#   time = request.GET.get('time')
#   if not time: time = ''
#   jeju_olle_list = JejuOlle.objects.filter(
#     time_info__contains=time)

#   return render(
#     request,
#     'thirdapp/jeju_olle.html',
#     {'jeju_olle_list': jeju_olle_list}
#   )