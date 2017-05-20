from django.conf.urls import url
from .views import DetailAccountPlan
from .views import ListAccountPlan
from .views import CreateAccountPlan
from .views import UpdateAccountPlan
from .views import DeleteAccountPlan


urlpatterns = [
                url(r'^List_AccountPlan$',
                    ListAccountPlan.as_view(), name='list_accountplan'),
                url(r'^List_AccountPlan/Crear/$',
                    CreateAccountPlan.as_view(),
                    name='create_accountplan'),
                url(r'^List_AccountPlan/Detail/(?P<pk>[0-9]+)/$',
                    DetailAccountPlan.as_view(),
                    name='detail_accountplan'),
                url(r'^AccountPlan/Update/(?P<pk>[0-9]+)/$',
                    UpdateAccountPlan.as_view(),
                    name='update_accountplan'),
                url(r'^AccountPlan/Delete/(?P<pk>[0-9]+)/$',
                    DeleteAccountPlan.as_view(),
                    name='delete_accountplan'),
                ]
