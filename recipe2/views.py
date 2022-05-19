from django.shortcuts import render
from django.views.generic.edit import FormView
from recipe2.forms import PostSearchForm
from django.db.models import Q
from .models import cookrecipe


class SearchFormView(FormView):
    form_class = PostSearchForm
    template_name = 'recipe2/search.html'

    def form_valid(self,form):
        schWord='%s'% self.request.POST['search_word']
        recipe2_list = cookrecipe.objects.filter(
            Q(title__icontains=schWord) | Q(descirption__icontains=schWord)|Q(content__icontains=schWord)
        ).distinct

        context ={}
        context['form'] = form
        context['search_term'] =schWord
        context['object_list'] = recipe2_list
        return render(self.request, self.template_name, context)


