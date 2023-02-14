from django.contrib import admin

from store.models import Brand, Type, Product


@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ("name",)}


@admin.register(Type)
class TypeAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ("name",)}


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ("name",)}