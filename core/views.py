from django.shortcuts import render

# Create your views here.
def home_page(request):
    return render(request, 'core/home_page.html', {})

def index(request):
    return render(request, 'core/index.html', {})

def sign_in(request):
    return render(request, 'core/index.html', {})