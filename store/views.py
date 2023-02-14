from django.views.generic import ListView, DetailView

from .models import Product, Type
from .utils import DataMixin


class MainPage(DataMixin, ListView):
    model = Product
    template_name = 'main_page.html'
    context_object_name = 'products'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Grocery Marketplace")
        print(dict(list(context.items()) + list(c_def.items())))
        return dict(list(context.items()) + list(c_def.items()))


class DetailsPage(DataMixin, DetailView):
    model = Product
    template_name = 'details_page.html'
    slug_url_kwarg = 'product_slug'
    context_object_name = 'product'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title=context['product'].name)
        return dict(list(context.items()) + list(c_def.items()))


class TypePage(DataMixin, ListView):
    model = Product
    template_name = 'main_page.html'
    context_object_name = 'products'
    allow_empty = False

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title=context['products'][0].type.name)
        c_def['type_selected'] = context['products'][0].type.id
        return dict(list(context.items()) + list(c_def.items()))
    
    def get_queryset(self):
        return Product.objects.filter(type__slug=self.kwargs['type_slug'])


class BrandPage(DataMixin, ListView):
    model = Product
    template_name = 'main_page.html'
    context_object_name = 'products'
    allow_empty = False

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title=context['products'][0].brand.name)
        c_def['brand_selected'] = context['products'][0].brand.id
        return dict(list(context.items()) + list(c_def.items()))
    
    def get_queryset(self):
        return Product.objects.filter(brand__slug=self.kwargs['brand_slug'])
