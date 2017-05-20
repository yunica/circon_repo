from django.conf.urls import url
from .views import ListExit
from .views import CreateExit
from .views import DetailExitDetail
from .views import UpdateExit
from .views import DeleteExit
from .views import Confirm
from .views import Delivered
from .views import Cancel

urlpatterns = [
                url(r'^List_Exit$', ListExit.as_view(),
                    name='list_exit'),
                url(r'^Exit/Create/$', CreateExit.as_view(),
                    name='create_exit'),
                url(r'^List_Exit/Detail/(?P<pk>[0-9]+)/$',
                    DetailExitDetail.as_view(), name='detail_exit'),
                url(r'^Exit/Update/(?P<pk>[0-9]+)/$',
                    UpdateExit.as_view(),
                    name='update_exit'),
                url(r'^Exit/Delete/(?P<pk>[0-9]+)/$',
                    DeleteExit.as_view(),
                    name='delete_exit'),
                url(r'^Exit/Confirm/(?P<pk>[0-9]+)/$',
                    Confirm.as_view(),
                    name='confirm_exit'),
                url(r'^Exit/Delivered/(?P<pk>[0-9]+)/$',
                    Delivered.as_view(),
                    name='delivered_exit'),
                url(r'^Exit/Cancel/(?P<pk>[0-9]+)/$', Cancel.as_view(),
                    name='cancel_exit'),
                ]
