from django.conf.urls import url
from .views import ListPurchase
from .views import CreatePurchase
from .views import DetailPurchaseDetail
from .views import UpdatePurchase
from .views import DeletePurchase
from .views import Confirm
from .views import Cancel
from .views import PurchasePDF


urlpatterns = [
                url(r'^List_Purchase$', ListPurchase.as_view(),
                    name='list_purchase'),
                url(r'^Purchase/Create/$', CreatePurchase.as_view(),
                    name='create_purchase'),
                url(r'^List_Purchase/Detail/(?P<pk>[0-9]+)/$',
                    DetailPurchaseDetail.as_view(),
                    name='detail_purchase'),
                url(r'^Purchase/Update/(?P<pk>[0-9]+)/$',
                    UpdatePurchase.as_view(), name='update_purchase'),
                url(r'^Purchase/Delete/(?P<pk>[0-9]+)/$',
                    DeletePurchase.as_view(), name='delete_purchase'),
                url(r'^Purchase/Confirm/(?P<pk>[0-9]+)/$',
                    Confirm.as_view(), name='confirm_purchase'),
                url(r'^Purchase/Cancel/(?P<pk>[0-9]+)/$',
                    Cancel.as_view(), name='cancel_purchase'),
                url(r'^Purchase/pdf/(?P<pk>[0-9]+)$',
                    PurchasePDF.as_view(), name='purchasepdf'),
                ]
