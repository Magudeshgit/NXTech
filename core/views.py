from django.shortcuts import render

def signup(request):
    return render(request, 'authentication/signup.html')

def signin(request):
    return render(request, 'authentication/signin.html')

def home(request):
    return render(request, 'core/index.html')