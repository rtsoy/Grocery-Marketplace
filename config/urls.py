"""config URL Configuration

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
from django.conf import settings
from django.conf.urls.static import static

from store.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', MainPage.as_view(), name='mainpage'),
    path('login/', LoginUser.as_view(), name='login'),
    path('logout', logout_user, name='logout'),
    path('register/', RegisterUser.as_view(), name='register'),
    path('product/<slug:brand_slug>/<slug:product_slug>', DetailsPage.as_view(), name='detailspage'),
    path('type/<slug:type_slug>', TypePage.as_view(), name='typepage'),
    path('brand/<slug:brand_slug>', BrandPage.as_view(), name='brandpage'),
    path('cart/', cart_detail, name='cart'),
    path('cart/remove/<int:id>', cart_remove, name='cart_remove'),
    path('?search=<str:search_query>', Search.as_view(), name='search'),
    path('cart/order-delivery', order_delivery, name='order_delivery')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)