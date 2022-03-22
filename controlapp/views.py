from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'controlapp/index.html')

def signup(request):
    return render(request, 'controlapp/signup.html')

def signin(request):
    return render(request, 'controlapp/signin.html')

def signout(requst):
    pass
