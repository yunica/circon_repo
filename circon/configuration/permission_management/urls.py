from django.conf.urls import url
from .views import ListUsersPermission
from .views import UpdatePermission
from .views import StartWarehouse
from .views import StartConfiguration
from .views import StartSales
from .views import StartPurchases
from .views import StartAccounting


urlpatterns = [
                url(r'^List_Users_Permission$',
                    ListUsersPermission.as_view(),
                    name='list_permission'),
                url(r'^Permission/Update/(?P<pk>[0-9]+)/$',
                    UpdatePermission.as_view(),
                    name='update_permission'),
                url(r'^Warehouse/$',
                    StartWarehouse.as_view(),
                    name='start_warehouse'),
                url(r'^Configuration/$',
                    StartConfiguration.as_view(),
                    name='start_configuration'),
                url(r'^Sales/$',
                    StartSales.as_view(),
                    name='start_sales'),
                url(r'^Purchases/$',
                    StartPurchases.as_view(),
                    name='start_purchases'),
                url(r'^Accounting/$',
                    StartAccounting.as_view(),
                    name='start_accounting'),
                ]
