from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.contrib.auth import logout, login
from django.shortcuts import redirect

from .models import Product, Type
from .utils import DataMixin
from .forms import RegisterUserForm, LoginUserForm


class MainPage(DataMixin, ListView):
    model = Product
    template_name = 'main_page.html'
    context_object_name = 'products'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Grocery Marketplace")
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


class RegisterUser(DataMixin, CreateView):
    form_class = RegisterUserForm
    template_name = 'register.html'
    success_url = reverse_lazy('mainpage')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Register')
        return dict(list(context.items()) + list(c_def.items()))

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('mainpage')


class LoginUser(DataMixin, LoginView):
    form_class = LoginUserForm
    template_name = 'login.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Login')
        return dict(list(context.items()) + list(c_def.items()))

    def get_success_url(self):
        return reverse_lazy('mainpage')


def logout_user(request):
    logout(request)
    return redirect('mainpage')