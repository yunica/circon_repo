from django.conf.urls import url
from .views import Index_View
from .views import ListProductsWeb
from .views import DetailProductsWeb
from .views import Contact
from .views import Start_Login

urlpatterns = [
                url(r'^$', Index_View.as_view(), name='index_view'),
                url(r'^List_ProductsWeb$', ListProductsWeb.as_view(),
                    name='list_productsweb_view'),
                url(r'^Detail_ProductsWeb/Detail/(?P<pk>[0-9]+)/$',
                    DetailProductsWeb.as_view(),
                    name='detail_productsweb_view'),
                url(r'^Contact$', Contact.as_view(),
                    name='contact_view'),
                url(r'^accounts/profile/$', Start_Login.as_view(),
                    name='start_login_view'),
                ]