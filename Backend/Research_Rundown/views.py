# views.py
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def home(request):
    return render(request, 'index.html')

def my_profile_page(request):
    return render(request, 'my-profile-page.html')

def signin_page(request):
    return render(request, 'signin-page.html')

def faq(request):
    return render(request, 'faq.html')
