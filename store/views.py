from django.shortcuts import render
from django.views.generic.base import View

from .models import Product, Type

class MainPage(View):
    def get(self, request):
        products = Product.objects.all().order_by('-id')
        data = {'products': products}
        return render(request, 'main_page.html', data)


class DetailsPage(View):
    def get(self, request, id):
        product = Product.objects.get(id=id)
        data = {'product': product}
        return render(request, 'details_page.html', data)


class FizzyDrinksPage(View):
    def get(self, request):
        fizzydrinks = Type.objects.get(id=3)
        products = Product.objects.filter(type=fizzydrinks)
        data = {'products': products}
        return render(request, 'main_page.html', data)


class DairyPage(View):
    def get(self, request):
        dairy = Type.objects.get(id=2)
        products = Product.objects.filter(type=dairy)
        data = {'products': products}
        return render(request, 'main_page.html', data)


class ChocolatePage(View):
    def get(self, request):
        chocolate = Type.objects.get(id=1)
        products = Product.objects.filter(type=chocolate)
        data = {'products': products}
        return render(request, 'main_page.html', data)