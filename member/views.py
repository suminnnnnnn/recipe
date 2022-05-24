from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from .forms import UserForm

def index(request):
    return render(request, 'base.html')

def home(requet):
    return render(requet,'base.html')

def static(request):
    return render(request, 'member/static.html')


def signup(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('member:index')
    else:
        form = UserForm()
    return render(request, 'member/signup.html', {'form': form})

def check(request):
    return render(request, 'background.html')

