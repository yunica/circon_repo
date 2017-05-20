from django.contrib import admin
from .models import Category
from import_export import resources
from import_export.admin import ImportExportModelAdmin


class CategoryResource(resources.ModelResource):

    class Meta:
        model = Category


class CategoryAdmin(ImportExportModelAdmin):
    resource_class = CategoryResource

admin.site.register(Category, CategoryAdmin)
