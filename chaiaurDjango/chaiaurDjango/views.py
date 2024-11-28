from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    # return HttpResponse("Hello, World, You are at homepage")
    return render(request, "website/index.html")

def about(request):
    return HttpResponse("Hello, World, You are at About page")

def contact(request):
    return HttpResponse("Hello, World, You are at Contact page")