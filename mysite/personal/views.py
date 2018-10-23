from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'personal/home.html')



def settings(request):
    return render(request, 'personal/Settings.html')

def signup(request):
    username = request.POST['username']
    email = request.POST['email']
    password = request.POST['password']
    return render(request, 'personal/signup.html')


