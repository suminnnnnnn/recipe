from random import random
from django.shortcuts import render,redirect
from django.views.generic.edit import FormView
from requests import request
from rest_framework.response import Response
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.views import APIView
from .serializers import RecipeSerializer
from recipe2.forms import PostSearchForm
from django.db.models import Q
from .models import recipe
from stockapp.models import Stock
from recipe2.recommendation import recommend_random
from django.forms import model_to_dict

#레시피 검색
class SearchFormView(FormView):
    form_class = PostSearchForm
    template_name = 'recipe2/search.html'

    def form_valid(self,form):
        schWord='%s'% self.request.POST['search_word']
        post_list = recipe.objects.filter(
            Q(ingredient__icontains=schWord)
            #icontains 대소문자 구분 X 단어 포함되어있는지 검사 -> filter조건은 Q객체로
        ).distinct

        context ={}
        context['form'] = form
        context['search_term'] =schWord
        context['object_list'] = post_list
        return render(self.request, self.template_name, context)


#재료기반레시피추천
def recipeStock(request):
    all_stock = Stock.objects.filter(stock_user=request.user)
    query = '''select * from recipe '''
    sep = ''
    prefix = 'where '
    
    for stock in all_stock:
        재고 = stock.stock_stock
        query += prefix + sep + "ingredient like '%%" + 재고 + "%%'"
        sep = ' and '
        prefix = ''

    result = recipe.objects.raw(query)
    # print(result)
    data_list = []
    for r in result:
        data = model_to_dict(r)
        data_list.append(data)

    result_dict = recommend_random()
    return render(
        request, 'recipe2/recommend.html', 
        {
            'data_list': data_list,
            'result_dict': result_dict
        }
    )

class RecipeStockAPIView(APIView):
    serializer_class = RecipeSerializer
    template_name = 'recommend.html'

    def get(self, request):
        all_stock = Stock.objects.filter(stock_user=request.user)
        query = '''select * from recipe '''
        sep = ''
        prefix = 'where '
        
        for stock in all_stock:
            재고 = stock.stock_stock
            query += prefix + sep + "ingredient like '%%" + 재고 + "%%'"
            sep = ' and '
            prefix = ''

        result = recipe.objects.raw(query)
        # print(result)
        data_list = []
        for r in result:
            data = model_to_dict(r)
            data_list.append(data)

        result_dict = recommend_random()


        return Response(data_list, self.template_name)
        return render


#랜덤레시피추천

class RandomAPIView(APIView):
    serializer_class = RecipeSerializer
    template_name = 'recommend.html'

    def get(self, request, *args, **kwargs):
        result_dict = recommend_random()
        print(result_dict)

  #      return Response(result_dict)
        return Response({'randomrecipe': result_dict})

