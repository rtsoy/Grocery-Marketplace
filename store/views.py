from django.views.generic import ListView, DetailView, CreateView
from django.views.generic.edit import FormMixin
from django.contrib.auth.views import LoginView
from django.contrib.auth.models import User
from django.db.models import Q, F, Sum
from django.urls import reverse_lazy
from django.contrib.auth import logout, login
from django.shortcuts import redirect, render, get_object_or_404

from .models import Product, Cart
from .utils import DataMixin, SearchMixin
from .forms import RegisterUserForm, LoginUserForm, CartAddProductForm, SearchBarForm

import json


class MainPage(DataMixin, SearchMixin, ListView):
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
    form_class = CartAddProductForm
    slug_url_kwarg = 'product_slug'
    context_object_name = 'product'

    def post(self, request, *, object_list=None, **kwargs):
        c = Cart.objects.filter(user=request.user, item=Product.objects.get(slug=kwargs['product_slug']))
        if c:
            c[0].quantity += int(request.POST['quantity'])
            c[0].save()
        else:   
            Cart.objects.create(
                user=request.user,
                item=Product.objects.get(slug=kwargs['product_slug']),
                quantity=request.POST['quantity']
            )
        return redirect('mainpage')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title=context['product'].name)
        return dict(list(context.items()) + list(c_def.items()))


class TypePage(DataMixin, SearchMixin, ListView):
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


class BrandPage(DataMixin, SearchMixin, ListView):
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


class Search(DataMixin, SearchMixin, ListView):
    model = Product
    template_name = 'main_page.html'
    context_object_name = 'products'
    

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Search:' + ' ' + str(self.kwargs['search_query']))
        return dict(list(context.items()) + list(c_def.items()))

    def get_queryset(self):
        return Product.objects.filter(
               Q(name__icontains=self.kwargs['search_query'])
            or Q(brand__name__icontains=self.kwargs['search_query'])
            or Q(type__name__icontains=self.kwargs['search_query']) 
        )


class LoginUser(DataMixin, LoginView):
    form_class = LoginUserForm
    template_name = 'login.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Login')
        return dict(list(context.items()) + list(c_def.items()))

    def get_success_url(self):
        return reverse_lazy('mainpage')


def cart_detail(request):
    if request.method == 'GET':
        cart = Cart.objects.filter(
            user=request.user
        ).annotate(
            total=F('item__price')*F('quantity')
        )

        total_price = Cart.objects.filter(
            user=request.user
        ).annotate(
            total=F('item__price')*F('quantity')
        ).aggregate(total_price = Sum('total'))['total_price']

        context = {
            'cart': cart,
            'total_price':total_price,
            'title':f"{request.user}'s shopping cart"
        }

        return render(request, 'cart.html', context)
    if request.method == 'POST':
        user = request.user
        item = Product.objects.get(pk=request.POST['item_id'])
        cart = get_object_or_404(Cart, user=user, item=item)
        cart.quantity = request.POST['quantity']
        if int(cart.quantity) > 0:
            cart.save()
        else:
            cart.delete()


def order_delivery(request):
    if request.method == 'GET':
        user = User.objects.get(username=request.user)

        cart = Cart.objects.filter(
                user=request.user
            ).annotate(
                total=F('item__price')*F('quantity')
            )

        total_price = Cart.objects.filter(
                user=request.user
            ).annotate(
                total=F('item__price')*F('quantity')
            ).aggregate(total_price = Sum('total'))['total_price']

        context = {
            'cart': cart,
            'total_price':total_price,
            'title': f"{request.user}'s order",
            'user': user,
        }
        return render(request, 'order.html', context)
    
    if request.method == 'POST':
        user = User.objects.get(username=request.user)
        cart = Cart.objects.filter(user=user)

        total_price = Cart.objects.filter(
                user=request.user
            ).annotate(
                total=F('item__price')*F('quantity')
            ).aggregate(total_price = Sum('total'))['total_price']

        order_data = {
            'first_name': request.POST['first-name'],
            'last_name': request.POST['last-name'],
            'address': request.POST['address'],
            'phone-number': request.POST['phone-number'],
            'products': [f'{i.item.brand.name} {i.item.name} | {i.item.price} x {i.quantity} = {i.item.price * i.quantity} KZT' for i in cart],
            'total_price': float(total_price),
        }

        with open('orders.json', 'a', encoding='utf-8') as json_file:
            json.dump(order_data, json_file, indent=4, ensure_ascii=False)
            json_file.write(',\n')

        cart.delete()

        return redirect('mainpage')


def cart_remove(request, id):
    Cart.objects.get(pk=id).delete()
    return redirect('cart')

def logout_user(request):
    logout(request)
    return redirect('mainpage')