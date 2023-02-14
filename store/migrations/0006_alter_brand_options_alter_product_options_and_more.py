# Generated by Django 4.1.5 on 2023-02-14 05:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0005_brand_remove_product_country_delete_country_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='brand',
            options={'ordering': ['name'], 'verbose_name': 'Brand', 'verbose_name_plural': 'Brands'},
        ),
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ['id'], 'verbose_name': 'Product', 'verbose_name_plural': 'Products'},
        ),
        migrations.AlterModelOptions(
            name='type',
            options={'ordering': ['name'], 'verbose_name': 'Type', 'verbose_name_plural': 'Types'},
        ),
        migrations.AddField(
            model_name='brand',
            name='slug',
            field=models.SlugField(default=None, max_length=255, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='product',
            name='slug',
            field=models.SlugField(default=None, max_length=255, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='type',
            name='slug',
            field=models.SlugField(default=None, max_length=255, null=True, unique=True),
        ),
    ]