from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect
import logging

from .models import *
logger = logging.getLogger(__name__)

menu = ['About Us', 'Add article', 'Contacts', 'Log In']
def index(request):
    logger.info('Index page accessed')
    posts = Women.objects.all()
    # return HttpResponse("WOMEN INDEX")
    return render(request, 'women/index.html', {'posts': posts, 'menu': menu, 'title': 'Home page'})

def about(request):
    logger.info('About page accessed')
    return render(request, 'women/about.html', {'title': 'About'})


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
