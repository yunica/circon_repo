from django.conf.urls import url
from .views import DetailCustomers
from .views import ListCustomers
from .views import CreateCustomers
from .views import UpdateCustomers
from .views import DeleteCustomers

urlpatterns = [
                url(r'^List_Customers$', ListCustomers.as_view(),
                    name='list_customers'),
                url(r'^List_Customers/Crear/$',
                    CreateCustomers.as_view(),
                    name='create_customers'),
                url(r'^List_Customers/Detail/(?P<pk>[0-9]+)/$',
                    DetailCustomers.as_view(),
                    name='detail_customers'),
                url(r'^Customers/Update/(?P<pk>[0-9]+)/$',
                    UpdateCustomers.as_view(),
                    name='update_customers'),
                url(r'^Customers/Delete/(?P<pk>[0-9]+)/$',
                    DeleteCustomers.as_view(),
                    name='delete_customers'),
                ]