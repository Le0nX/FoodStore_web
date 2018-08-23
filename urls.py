"""FoodStore URL Configuration

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
from foodstoreapp import views
from django.contrib.auth import views as auth_views

from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.home, name='home'),
    url(r'^foodstore/sign-in/$', auth_views.login,
        {'template_name': 'foodstore/sign_in.html'},
        name='foodstore-sign-in'),
    url(r'^foodstore/sign-out', auth_views.logout,
        {'next_page': '/'},
        name='foodstore-sign-out'),
    url(r'^foodstore/sign-up', views.foodstore_sign_up,
        name='foodstore-sign-up'),
    url(r'^foodstore/$', views.foodstore_home, name='foodstore-home')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
