from django.shortcuts import HttpResponse

# Create your views here.
def home(request):
    return HttpResponse('Home')

def login(request):
    return HttpResponse('Login')

def register(request):
    return HttpResponse('Register')

