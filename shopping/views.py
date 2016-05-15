# coding:utf-8
from django.shortcuts import render, render_to_response
from django.http import HttpResponseRedirect, JsonResponse, HttpResponse
from .models import *
import json


# Create your views here.


def index(request):
    email = request.session.get("email", "")
    if email:
        return render(request, "index.html", {"username": User.objects.get(email=email).name, "logout": "logout"})
    else:
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


def user_login(request):
    email = request.POST["email"]
    if request.is_ajax() and request.method == "POST":
        t = User.objects.filter(email=email)
        return JsonResponse(len(t), safe=False)
    if request.method == "POST" and not request.is_ajax():
        request.session["email"] = email
        return HttpResponseRedirect("/index")


def logout(request):
    del request.session["email"]
    return HttpResponseRedirect("/index")


def test_pwd(request):
    if request.is_ajax():
        email = request.POST["email"]
        password = request.POST["password"]
        if User.objects.get(email=email).pwd == password:
            return JsonResponse(1, safe=False)
        else:
            return JsonResponse(0, safe=False)


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
