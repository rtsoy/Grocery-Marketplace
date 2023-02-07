from django.contrib import admin

from store.models import Brand, Type, Product


@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    pass


@admin.register(Type)
class TypeAdmin(admin.ModelAdmin):
    pass


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    pass

