from django.shortcuts import render

from django.http import HttpResponse


# Create your views here.
def sai6(request):
    return HttpResponse("hai hello this is me")

def sai7(request):
    return HttpResponse("<h1>hello this is me</h1>")

def sai8(request):
    return HttpResponse("<h2>hai this is me</h2>")

def sai9(request):
    return HttpResponse("<h1>saimani this is me</h1>")

def sai10(request):
    return HttpResponse ("<h1><i><marquee> hello saimanikanta his is also me</marquee></i></h1>")

