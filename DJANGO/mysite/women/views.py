from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect
import logging

from .forms import AddPostForm
from .models import *

logger = logging.getLogger(__name__)

menu = [{'title': 'About Us', 'url_name': 'about'},
        {'title': 'Add article', 'url_name': 'add_page'},
        {'title': 'Contacts', 'url_name': 'contact'},
        {'title': 'Log In', 'url_name': 'login'}, ]


def index(request):
    logger.info('Index page accessed')
    posts = Women.objects.all()
    cats = Category.objects.all()
    context = {'posts': posts,
               'cats': cats,
               'menu': menu,
               'title': 'Home page',
               'cat_selected': 0, }
    # return HttpResponse("WOMEN INDEX")
    return render(request, 'women/index.html', context=context)


def about(request):
    logger.info('About page accessed')
    return render(request, 'women/about.html', {'title': 'About', 'menu': menu})


def addpage(request):
    if request.method == 'POST':
        form = AddPostForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            try:
                Women.objects.create(**form.cleaned_data)
                return redirect('home')
            except:
                form.add_error(None, "Ошибка добавления поста")
    else:
        form = AddPostForm({'title': 'AAAAAA'})
    return render(request, 'women/addpage.html', {'form': form, 'menu': menu, 'title': 'Add article'})


def contact(request):
    return HttpResponse("Contacts")


def login(request):
    return HttpResponse("Login")


def show_post(request, post_id):
    return HttpResponse(f"Article #{post_id}")


def show_category(request, cat_id):
    posts = Women.objects.filter(cat_id=cat_id)
    cats = Category.objects.all()
    if len(posts) == 0:
        raise Http404()

    context = {'posts': posts,
               'cats': cats,
               'menu': menu,
               'title': 'Home page',
               'cat_selected': cat_id, }

    return render(request, 'women/index.html', context=context)


# def categories(request, cat_id):
#     if request.GET:
#         print(request.GET)
#     if request.POST:
#         print(request.POST)
#     return HttpResponse(f"<h1> CATEGORIES {cat_id} </h1>")


def archive(request, year):
    if int(year) > 2023:
        # raise Http404()
        # return redirect('/')
        return redirect('home', permanent=True)
    return HttpResponse(f"<h1> ARCHIVE {year} </h1>")


def pageNotFound(request, exeption):
    return HttpResponseNotFound(f"<h1> PAGE NOT FOUND! </h1>")
