from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse


# Create your views here.


def index(request):
    return render(request, "index.html")


def register(request):
    return render(request, "register.html")


def blog(request):
    return render(request, "blog.html")


def products(request):
    return render(request, "products.html")


def login(request):
    return render(request, "login.html")


def blog_single(request):
    return render(request, "blog_single.html")


def contact(request):
    return render(request, "contact.html")


def single(request):
    return render(request, "single.html")


def checkout(request):
    return render(request, "checkout.html")
