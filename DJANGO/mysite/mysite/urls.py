"""
Список `urlpatterns` направляет URL-адреса в представления. Для получения дополнительной информации см.:
     https://docs.djangoproject.com/en/4.2/topics/http/urls/
Примеры:
Представления функций
     1. Добавьте импорт: из представлений импорта my_app.
     2. Добавьте URL-адрес в urlpatterns: path('',views.home, name='home')
Представления на основе классов
     1. Добавляем импорт: fromother_app.views import Home
     2. Добавьте URL-адрес в urlpatterns: path('', Home.as_view(), name='home')
Включение другого URLconf
     1. Импортируйте функцию include(): из django.urls import include, путь
     2. Добавьте URL-адрес в urlpatterns: path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

# import settings
from women.views import pageNotFound

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('women.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = pageNotFound
