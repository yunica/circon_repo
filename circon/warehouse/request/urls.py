from django.conf.urls import url
from .views import ListRequest
from .views import CreateRequest
from .views import DetailRequestDetail
from .views import UpdateRequest
from .views import DeleteRequest
from .views import Confirm
from .views import Delivered
from .views import Cancel


urlpatterns = [
                url(r'^List_Request$', ListRequest.as_view(),
                    name='list_request'),
                url(r'^Request/Create/$', CreateRequest.as_view(),
                    name='create_request'),
                url(r'^List_Request/Detail/(?P<pk>[0-9]+)/$',
                    DetailRequestDetail.as_view(),
                    name='detail_request'),
                url(r'^Request/Update/(?P<pk>[0-9]+)/$',
                    UpdateRequest.as_view(), name='update_request'),
                url(r'^Request/Delete/(?P<pk>[0-9]+)/$',
                    DeleteRequest.as_view(), name='delete_request'),
                url(r'^Request/Confirm/(?P<pk>[0-9]+)/$',
                    Confirm.as_view(), name='confirm_request'),
                url(r'^Request/Delivered/(?P<pk>[0-9]+)/$',
                    Delivered.as_view(), name='delivered_request'),
                url(r'^Request/Cancel/(?P<pk>[0-9]+)/$',
                    Cancel.as_view(), name='cancel_request'),
                ]
