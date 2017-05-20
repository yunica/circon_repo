from django.conf.urls import url
from .views import DetailProviders
from .views import ListProviders
from .views import CreateProviders
from .views import UpdateProviders
from .views import DeleteProviders

urlpatterns = [
                url(r'^List_Providers$', ListProviders.as_view(),
                    name='list_providers'),
                url(r'^List_Providers/Crear/$',
                    CreateProviders.as_view(), name='create_providers'),
                url(r'^List_Providers/Detail/(?P<pk>[0-9]+)/$',
                    DetailProviders.as_view(), name='detail_providers'),
                url(r'^Providers/Update/(?P<pk>[0-9]+)/$',
                    UpdateProviders.as_view(), name='update_providers'),
                url(r'^Providers/Delete/(?P<pk>[0-9]+)/$',
                    DeleteProviders.as_view(), name='delete_providers'),
              ]
