from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect


def index(request):
    return HttpResponse("WOMEN INDEX")


def categories(request, cat_id):
    if request.GET:
        print(request.GET)
    if request.POST:
        print(request.POST)
    return HttpResponse(f"<h1> CATEGORIES {cat_id} </h1>")

def archive(request, year):
    if int(year) > 2023:
        # raise Http404()
        # return redirect('/')
        return redirect('home', permanent=True)
    return HttpResponse(f"<h1> ARCHIVE {year} </h1>")

def pageNotFound(request, exeption):
    return HttpResponseNotFound(f"<h1> PAGE NOT FOUND! </h1>")
