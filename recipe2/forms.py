from django import forms

class PostSearchForm(forms.Form):
    search_word = forms.CharField(label = '재료를 입력하세요')