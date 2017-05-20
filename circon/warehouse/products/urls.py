from django.conf.urls import url
from .views import DetailProducts
from .views import ListProducts
from .views import CreateProducts
from .views import UpdateProducts
from .views import DeleteProducts


urlpatterns = [
                url(r'^List_Products$', ListProducts.as_view(),
                    name='list_products'),
                url(r'^List_Products/Create/$',
                    CreateProducts.as_view(), name='create_products'),
                url(r'^List_Products/Detail/(?P<pk>[0-9]+)/$',
                    DetailProducts.as_view(), name='detail_products'),
                url(r'^Products/Update/(?P<pk>[0-9]+)/$',
                    UpdateProducts.as_view(), name='update_products'),
                url(r'^Products/Delete/(?P<pk>[0-9]+)/$',
                    DeleteProducts.as_view(), name='delete_products'),
               ]
