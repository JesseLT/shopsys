# coding:utf-8
from django.shortcuts import render, render_to_response
from django.http import HttpResponseRedirect, JsonResponse, HttpResponse
from .models import *
import json


# Create your views here.


def index(request):
    return render(request, "index.html")


def register(request):
    return render(request, "register.html")


def new_user(request):
    name = request.POST["name"]
    email = request.POST["email"]
    pwd = request.POST["password"]

    u = User(name=name, email=email, pwd=pwd)
    u.save()

    return HttpResponseRedirect("/login")
    # return HttpResponse(name)


def test_email(request):
    if request.is_ajax():
        if request.method == "POST":
            email = request.POST["email"]
            t = User.objects.filter(email=email)
            return JsonResponse(len(t), safe=False)


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


def test(request):
    return render(request, "test.html")


def test_ajax(request):
    if request.method == 'POST' and request.is_ajax():
        name = request.POST.get('value')
        return JsonResponse("success", safe=False)
