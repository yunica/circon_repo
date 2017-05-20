from django.conf.urls import url
from .views import ListLogs
from .views import LogsProducts
from .views import LogsRequest
from .views import LogsRequestDetail
from .views import LogsUnitsMeasures
from .views import LogsCategory


urlpatterns = [
               url(r'^ListLogs$', ListLogs.as_view(),
                   name='list_logs'),
               url(r'^LogsProducts$', LogsProducts.as_view(),
                   name='logs_products'),
               url(r'^LogsRequest', LogsRequest.as_view(),
                   name='logs_request'),
               url(r'^LogsRequestDetail', LogsRequestDetail.as_view(),
                   name='logs_requestdetail'),
               url(r'^LogsUnitsMeasures$', LogsUnitsMeasures.as_view(),
                   name='logs_unitsmeasures'),
               url(r'^LogsCategory$', LogsCategory.as_view(),
                   name='logs_category'),
               ]
