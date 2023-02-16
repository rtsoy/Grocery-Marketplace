from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from .models import Cart, Product


class RegisterUserForm(UserCreationForm):
    username = forms.CharField(label='Username', widget=forms.TextInput(attrs={'class': 'form-input'}))
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'class': 'form-input'}))
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'form-input'}))
    password2 = forms.CharField(label='Enter the same password as before, for verification', widget=forms.PasswordInput(attrs={'class': 'form-input'}))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label='Username', widget=forms.TextInput(attrs={'class': 'form-input'}))
    password = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'form-input'}))


class CartAddProductForm(forms.ModelForm):
    quantity = forms.IntegerField(widget=forms.NumberInput(attrs={'size': '2', 'value': '1', 'min':1, 'max':100}))

    class Meta:
        model = Cart
        fields = ['quantity']


class SearchBarForm(forms.ModelForm):
    search_query = forms.CharField(label="", widget=forms.TextInput())

    class Meta:
        model = Product
        fields = ['search_query']