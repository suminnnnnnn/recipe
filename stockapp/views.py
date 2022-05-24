from ast import Add
from ssl import MemoryBIO
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.models import User
from member.models import Member
from .models import Add ,Stock


def add(request):
  if request.method == 'POST':
    Member = User.objects.get(username=request.user.username)
    
    Add_stock = request.POST.get('Add_stock')
    Add_amount = request.POST.get('Add_amount')
    Add_month = request.POST.get('Add_month')
    url_start = 'https://www.coupang.com/np/search?component=&q='
    url_end = '&channel=user'
    url_all = url_start + Add_stock + url_end
    
    add = Add(Add_stock=Add_stock, Add_amount=Add_amount,Add_month=Add_month,Add_user=Member)
    stock = Stock(stock_stock=Add_stock, stock_amount=Add_amount,stock_month=Add_month,stock_urls=url_all,stock_user=Member)
    add.save()
    stock.save()

    return render(request, 'stockapp/message.html',{}) 
  return render(request, 'stockapp/add.html', {})

def stock(request):
  stock_list = Stock.objects.filter(stock_user=User.objects.get(username=request.user.username))
  return render(request,'stockapp/stock.html',{'stock_list': stock_list})


# def stock(request):
#   if (stock_user!=User.objects.get(username=request.user.username))
#     return render(request,'member/login.html')
#   else     
#   stock_list = Stock.objects.filter(stock_user=User.objects.get(username=request.user.username))
#   return render(request,'stockapp/stock.html',{'stock_list': stock_list})

  
# User.objects.get(username=request.user.username)


# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import status
# from .serializers import StockSerializer
# from .models import Stock
# from rest_framework import permissions


# class StockView(APIView):
#     def get(self, request):
#         queryset = Stock.objects.filter(user_id=request.user.id)
#         print(request.user.id)
#         serializer = StockSerializer(queryset, many=True)
#         return Response(serializer.data)

#     def post(self, request):
#         # _mutable = request.data._mutable
#         # request.data._mutable = True
#         # request.data.update({"user_id": request.user.id})
#         # request.data._mutable = _mutable
#         serializer = StockSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# class StockDetailView(APIView):
#     def get(self, request, stock_id):
#         # serializer = StockSerializer(data=request.data)
#         stock = Stock.objects.filter(id=stock_id)
#         if stock:
#             serializer = StockSerializer(stock, many=True)
#             return Response(serializer.data)
#         else:
#             return Response({'Error': "Can't find stock"}, status=status.HTTP_404_NOT_FOUND)

#     def put(self, request, stock_id):
#         stock = Stock.objects.get(id=stock_id)
#         if stock:
#             serializer = StockSerializer(stock, data=request.data)
#             if request.user.id != stock.user_id.id:
#                 return Response({'Error': "Not your stock"}, status=status.HTTP_400_BAD_REQUEST)
#             if serializer.is_valid():
#                 serializer.save()
#                 return Response(serializer.data, status=status.HTTP_201_CREATED)
#             else:
#                 return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#         else:
#             return Response({'Error': "Can't find stock"}, status=status.HTTP_404_NOT_FOUND)

#     def delete(self, request, stock_id):
#         stock = Stock.objects.get(id=stock_id)
#         if stock:
#             if request.user.id != stock.user_id.id:
#                 return Response({'Error': "Not your stock"}, status=status.HTTP_400_BAD_REQUEST)
#             else:
#                 stock.delete()
#                 return Response(status=status.HTTP_204_NO_CONTENT)
#         else:
#             return Response({'Error': "Can't find stock"}, status=status.HTTP_404_NOT_FOUND)


