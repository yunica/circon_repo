from django.conf.urls import url
from circon.warehouse.category.views import DetailCategory
from circon.warehouse.category.views import ListCategory
from circon.warehouse.category.views import CreateCategory
from circon.warehouse.category.views import UpdateCategory
from circon.warehouse.category.views import DeleteCategory


urlpatterns = [
                url(r'^List_Category$', ListCategory.as_view(),
                    name='list_category'),
                url(r'^List_Category/Create/$',
                    CreateCategory.as_view(),
                    name='create_category'),
                url(r'^List_Category/Detail/(?P<pk>[0-9]+)/$',
                    DetailCategory.as_view(), name='detail_category'),
                url(r'^Category/Update/(?P<pk>[0-9]+)/$',
                    UpdateCategory.as_view(), name='update_category'),
                url(r'^Category/Delete/(?P<pk>[0-9]+)/$',
                    DeleteCategory.as_view(), name='delete_category'),
                ]
