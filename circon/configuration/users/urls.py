from django.conf.urls import url
from .views import Start_View
from .views import ListUsers
from .views import DetailUsers
from .views import CreateUsers
from .views import DeleteUsers
from .views import UpdateUsers
from .views import ChangePassword

urlpatterns = [
                url(r'^Admin$', Start_View.as_view(),
                    name='start_view'),
                url(r'^List_Users$', ListUsers.as_view(),
                    name='list_users'),
                url(r'^Users/Create/$', CreateUsers.as_view(),
                    name='create_user'),
                url(r'^List_Users/Detail/(?P<pk>[0-9]+)/$',
                    DetailUsers.as_view(), name='detail_user'),
                url(r'^Users/Update/(?P<pk>[0-9]+)/$',
                    UpdateUsers.as_view(), name='update_user'),
                url(r'^Users/Delete/(?P<pk>[0-9]+)/$',
                    DeleteUsers.as_view(), name='delete_user'),
                url(r'^Change_Password/(?P<pk>[0-9]+)/$',
                    ChangePassword.as_view(), name='change_password'),
                ]
