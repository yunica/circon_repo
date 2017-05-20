from django.conf.urls import url
from .views import ListSale
from .views import CreateSale
from .views import DetailSaleDetail
from .views import UpdateSale
from .views import DeleteSale
from .views import Confirm
from .views import Cancel

urlpatterns = [
                url(r'^List_Sale$', ListSale.as_view(),
                    name='list_sale'),
                url(r'^Sale/Create/$', CreateSale.as_view(),
                    name='create_sale'),
                url(r'^List_Sale/Detail/(?P<pk>[0-9]+)/$',
                    DetailSaleDetail.as_view(), name='detail_sale'),
                url(r'^Sale/Update/(?P<pk>[0-9]+)/$',
                    UpdateSale.as_view(), name='update_sale'),
                url(r'^Sale/Delete/(?P<pk>[0-9]+)/$',
                    DeleteSale.as_view(), name='delete_sale'),
                url(r'^Sale/Confirm/(?P<pk>[0-9]+)/$',
                    Confirm.as_view(), name='confirm_sale'),
                url(r'^Sale/Cancel/(?P<pk>[0-9]+)/$',
                    Cancel.as_view(), name='cancel_sale'),
                ]
