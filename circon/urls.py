"""circon URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [

    url(r'^admin/', include(admin.site.urls)),

    # Configurations
    url(r'^', include('circon.configuration.users.urls')),
    url(r'^', include('circon.configuration.groups.urls')),
    url(r'^', include('circon.configuration.mycompany.urls')),
    url(r'^', include('circon.configuration.backup.urls')),
    url(r'^', include('circon.configuration.logs.urls')),
    url(r'^', include('circon.configuration.authenticate.urls')),
    url(r'^', include('circon.configuration.permission_management.urls')),
    url(r'^', include('circon.configuration.translation.urls')),
    url(r'^', include('social.apps.django_app.urls', namespace='social')),

    # Warehouse
    url(r'^', include('circon.warehouse.units_measures.urls')),
    url(r'^', include('circon.warehouse.products.urls')),
    url(r'^', include('circon.warehouse.inventory.urls')),
    url(r'^', include('circon.warehouse.category.urls')),
    url(r'^', include('circon.warehouse.entry.urls')),
    url(r'^', include('circon.warehouse.exit.urls')),
    url(r'^', include('circon.warehouse.request.urls')),

    # Purchases
    url(r'^', include('circon.purchases.providers.urls')),
    url(r'^', include('circon.purchases.purchase.urls')),


    # Sales
    url(r'^', include('circon.sales.sale.urls')),
    url(r'^', include('circon.sales.customers.urls')),

    # Accounting
    url(r'^', include('circon.accounting.accountplan.urls')),

    # Website
    url(r'^', include('circon.website.home.urls')),
    url(r'^accounts/', include('registration.backends.default.urls')),
    url(r'^', include('circon.website.api.urls')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
