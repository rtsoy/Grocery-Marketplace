from django.contrib.auth.models import User
from django.db import models


class Brand(models.Model):
    name = models.CharField(max_length=64, null=False)
    slug = models.SlugField(max_length=255, unique=True, db_index=True, null=True, default=None)
    country = models.CharField(max_length=64, null=False)

    class Meta:
        verbose_name = 'Brand'
        verbose_name_plural = 'Brands'
        ordering = ['name']

    def __str__(self) -> str:
        return f'{self.name} : {self.country}'


class Type(models.Model):
    name = models.CharField(max_length=32, null=False)
    slug = models.SlugField(max_length=255, unique=True, db_index=True, null=True, default=None)

    class Meta:
        verbose_name = 'Type'
        verbose_name_plural = 'Types'
        ordering = ['name']

    def __str__(self) -> str:
        return f'{self.name}'


class Product(models.Model):
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, null=False)
    name = models.CharField(max_length=64, null=False)
    slug = models.SlugField(max_length=255, unique=True, db_index=True, null=True, default=None)
    description = models.TextField(max_length=1024, null=False)
    protein = models.DecimalField(max_digits=4, decimal_places=1 ,null=False)
    fat = models.DecimalField(max_digits=4, decimal_places=1 ,null=False)
    carbohydrates = models.DecimalField(max_digits=4, decimal_places=1 ,null=False)
    type = models.ForeignKey(Type, on_delete=models.CASCADE, null=False)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    img = models.ImageField(upload_to='image/%Y')

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'
        ordering = ['id']

    def __str__(self) -> str:
        return f'{self.brand.name} : {self.name} : {self.price} KZT'
    
    
class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    item = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

    class Meta:
        verbose_name = 'Cart'
        verbose_name_plural = 'Carts'
        ordering = ['-id']

    def __str__(self) -> str:
        return f'{self.user} -> {self.item} [{self.quantity}]'
