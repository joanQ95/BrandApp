from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request,'home.html')

def payment(request):
    return render(request,'account/payment.html')