"""ShareParking URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
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
from django.http import HttpResponse
from Main.views import test, sign_up, order, find_parking
from Main.page import page, order_info

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', test),
    url(r'sign-up', sign_up),
    url(r'^order$', order),
    url(r'find-parking', find_parking),
    url(r'page', order_info),
]



