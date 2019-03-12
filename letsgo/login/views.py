from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm


def index(request):
    return render(request, 'login/home.html')

def about(request):
    return render(request, 'login/About.html')
def support(request):
    return render(request,'login/Support.html')

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request,user)
            return redirect('/About')
    else:
        form = UserCreationForm()
    return render(request, 'login/signup.html', {'form': form})
