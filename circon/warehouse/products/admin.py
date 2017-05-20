from django.contrib import admin
from .models import Products
from import_export import resources
from import_export.admin import ImportExportModelAdmin


class ProductsResource(resources.ModelResource):

    class Meta:
        model = Products


class ProductsAdmin(ImportExportModelAdmin):
    resource_class = ProductsResource

admin.site.register(Products, ProductsAdmin)
