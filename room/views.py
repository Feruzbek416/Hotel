from django.shortcuts import render

# Create your views here.

def Hotel(request):
    return render(request,'room/index.html')