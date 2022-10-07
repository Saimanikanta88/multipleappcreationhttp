"""project2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from app2.views import *
from app3.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('sai1/',sai1,name='sai1'),
    path('sai2/',sai2,name='sai2'),
    path('sai3/',sai3,name='sai3'),
    path('sai4/',sai4,name='sai4'),
    path('sai5/',sai5,name='sai5'),
    path('sai6/',sai6,name='sai6'),
    path('sai7/',sai7,name='sai7'),
    path('sai8/',sai8,name='sai8'),
    path('sai9/',sai9,name='sai9'),
    path('sai10/',sai10,name='sai10'),
]
