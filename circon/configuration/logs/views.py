from django.views.generic import ListView
from django.views.generic import TemplateView
from pure_pagination.mixins import PaginationMixin
from circon.warehouse.products.models import Products
from circon.warehouse.category.models import Category
from circon.warehouse.units_measures.models import UnitsMeasures
from circon.warehouse.request.models import Request
from circon.warehouse.request.models import RequestDetail


class ListLogs(PaginationMixin, TemplateView):
    template_name = 'configuration/logs/listlogs.html'
    paginate_by = 10


class LogsProducts(PaginationMixin, ListView):
    template_name = 'configuration/logs/logsproducts.html'
    queryset = Products.audit_log.all()
    paginate_by = 10


class LogsRequest(PaginationMixin, ListView):
    template_name = 'configuration/logs/logsrequest.html'
    queryset = Request.audit_log.all()
    paginate_by = 10


class LogsRequestDetail(PaginationMixin, ListView):
    template_name = 'configuration/logs/logsrequestdetail.html'
    queryset = RequestDetail.audit_log.all()
    paginate_by = 10



class LogsUnitsMeasures(PaginationMixin, ListView):
    template_name = 'configuration/logs/logsunitsmeasures.html'
    queryset = UnitsMeasures.audit_log.all()
    paginate_by = 10


class LogsCategory(PaginationMixin, ListView):
    template_name = 'configuration/logs/logscategory.html'
    queryset = Category.audit_log.all()
    paginate_by = 10
