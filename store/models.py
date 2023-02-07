from django.db import models


class Country(models.Model):
    name = models.CharField(max_length=64, null=False)

    class Meta:
        verbose_name = 'Country'
        verbose_name_plural = 'Countries'

    def __str__(self) -> str:
        return f'{self.name}'


class Type(models.Model):
    name = models.CharField(max_length=32, null=False)

    class Meta:
        verbose_name = 'Type'
        verbose_name_plural = 'Types'

    def __str__(self) -> str:
        return f'{self.name}'


class Product(models.Model):
    brand = models.CharField(max_length=64, null=False)
    name = models.CharField(max_length=64, null=False)
    description = models.TextField(max_length=1024, null=False)
    country = models.ForeignKey(Country, on_delete=models.CASCADE, null=False)
    protein = models.DecimalField(max_digits=4, decimal_places=1 ,null=False)
    fat = models.DecimalField(max_digits=4, decimal_places=1 ,null=False)
    carbohydrates = models.DecimalField(max_digits=4, decimal_places=1 ,null=False)
    type = models.ForeignKey(Type, on_delete=models.CASCADE, null=False)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    img = models.ImageField(upload_to='image/%Y')

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'

    def __str__(self) -> str:
        return f'{self.name} : {self.country} : {self.price} KZT'
    
    
    
