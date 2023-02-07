from django.contrib import admin

from store.models import Country, Type, Product


@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    pass


@admin.register(Type)
class TypeAdmin(admin.ModelAdmin):
    pass


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    pass

