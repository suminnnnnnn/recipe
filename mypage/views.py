from django.shortcuts import render
from mypage.models import Stock
from .models import Stock
def mystock(request):
    stock_list = Stock.objects.all()
    return render(
    request,
    'mypage/mystock.html',
    {'stock_list': stock_list}
    )

def mypage(request):
    return render(request,'mypage.html')
