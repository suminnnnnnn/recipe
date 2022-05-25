from django.shortcuts import render,redirect
from django.views.generic.edit import FormView
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import RecipeSerializer
from recipe2.forms import PostSearchForm
from django.db.models import Q
from .models import recipe
from stockapp.models import Stock
from recipe2.recommendation import recommend_random



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

#랜덤레시피추천
class RandomAPIView(APIView):
    serializer_class = RecipeSerializer

    def get(self, request, *args, **kwargs):
        result_dict = recommend_random()
        print(result_dict)
        return Response(result_dict)