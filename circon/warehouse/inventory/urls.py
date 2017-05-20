from django.conf.urls import url
from .views import Inventory
from .views import SearchCategory
from .views import ProductsAutocomplete


urlpatterns = [
                url(r'^List_Inventory$', Inventory.as_view(),
                    name='list_inventory'),
                url(r'^SearchCategory/(?P<pk>[0-9]+)/$', SearchCategory.as_view(),
                    name='search_category'),
                url(r'^products-autocomplete/$', ProductsAutocomplete.as_view(),
                    name='products-autocomplete'),
                ]