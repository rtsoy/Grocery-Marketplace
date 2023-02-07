from django.shortcuts import render
from django.views.generic.base import View

from .models import Product

class MainPage(View):
    def get(self, request):
        products = Product.objects.all().order_by('-id')
        data = {'products': products}
        return render(request, 'main_page.html', data)
