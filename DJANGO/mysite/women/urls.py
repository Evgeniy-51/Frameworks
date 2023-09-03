from django.urls import path, re_path

from women.views import *

urlpatterns = [
    path('', index, name='home'),  # http://127.0.0.1:8000/
    path('cat/<int:cat_id>/', categories),  # http://127.0.0.1:8000/cat/
    re_path(r'^archive/(?P<year>[0-9]{4})/', archive)
]
