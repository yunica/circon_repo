from django.conf.urls import url
from .views import ListMyCompany
from .views import DetailMyCompany
from .views import CreateMyCompany
from .views import DeleteMyCompany
from .views import UpdateMyCompany


urlpatterns = [
                url(r'^List_MyCompany$', ListMyCompany.as_view(),
                    name='list_mycompany'),
                url(r'^MyCompany/Create/$', CreateMyCompany.as_view(),
                    name='create_mycompany'),
                url(r'^List_MyCompany/Detail/(?P<pk>[0-9]+)/$',
                    DetailMyCompany.as_view(), name='detail_mycompany'),
                url(r'^MyCompany/Update/(?P<pk>[0-9]+)/$',
                    UpdateMyCompany.as_view(), name='update_mycompany'),
                url(r'^MyCompany/Delete/(?P<pk>[0-9]+)/$',
                    DeleteMyCompany.as_view(), name='delete_mycompany'),
                ]
