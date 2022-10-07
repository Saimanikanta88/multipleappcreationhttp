from django.shortcuts import render

from django.http import HttpResponse
# Create your views here.

def sai1(request):
    return HttpResponse("hai hello this is me")

def sai2(request):
    return HttpResponse("<h1>hello this is me</h1>")

def sai3(request):
    return HttpResponse("<h2>hai this is me</h2>")

def sai4(request):
    return HttpResponse("<h1>saimani this is me</h1>")

def sai5(request):
    return HttpResponse ("<h1><marquee> hello saimanikanta his is also me</marquee></h1>")

