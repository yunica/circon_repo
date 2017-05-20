from django.conf.urls import url
from .views import ListEntry
from .views import CreateEntry
from .views import DetailEntryDetail
from .views import UpdateEntry
from .views import DeleteEntry
from .views import Confirm
from .views import Received
from .views import Cancel

urlpatterns = [
                url(r'^List_Entry$', ListEntry.as_view(),
                    name='list_entry'),
                url(r'^Entry/Create/$', CreateEntry.as_view(),
                    name='create_entry'),
                url(r'^List_Entry/Detail/(?P<pk>[0-9]+)/$',
                    DetailEntryDetail.as_view(),
                    name='detail_entry'),
                url(r'^Entry/Update/(?P<pk>[0-9]+)/$',
                    UpdateEntry.as_view(), name='update_entry'),
                url(r'^Entry/Delete/(?P<pk>[0-9]+)/$',
                    DeleteEntry.as_view(),
                    name='delete_entry'),
                url(r'^Entry/Confirm/(?P<pk>[0-9]+)/$',
                    Confirm.as_view(),
                    name='confirm_entry'),
                url(r'^Entry/Received/(?P<pk>[0-9]+)/$',
                    Received.as_view(),
                    name='received_entry'),
                url(r'^Entry/Cancel/(?P<pk>[0-9]+)/$', Cancel.as_view(),
                    name='cancel_entry'),
                ]
