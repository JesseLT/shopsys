"""shopsys URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from shopping import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^index', views.index, name="index"),
    url(r'^login', views.login, name="login"),

    url(r'^register', views.register, name="register"),
    url(r'^new_user', views.new_user, name="new_user"),
    url(r'^test_email', views.test_email, name="test_email"),

    url(r'^products', views.products, name="products"),
    url(r'^single', views.single, name="single"),
    url(r'^blog', views.blog, name="blog"),
    url(r'^blog_single', views.blog_single, name="blog_single"),
    url(r'^contact', views.contact, name="contact"),
    url(r'^checkout', views.checkout, name="checkout"),

    url(r'^test', views.test, name="test"),
    url(r'^test_ajax', views.test_ajax, name="test_ajax"),
]
