from django.views.generic import ListView
from django.views.generic import TemplateView
from django.contrib.auth.models import User
from django.views.generic.edit import UpdateView
from django.core.urlresolvers import reverse
from pure_pagination.mixins import PaginationMixin
from .forms import CreateForm


class ListUsersPermission(PaginationMixin, ListView):
    template_name = 'configuration/permission_management/list.html'
    model = User
    paginate_by = 10


class UpdatePermission(UpdateView):
    template_name = 'configuration/permission_management/update.html'
    model = User
    form_class = CreateForm

    def get_success_url(self):
        return reverse('list_permission')


class StartWarehouse(TemplateView):
    template_name = 'warehouse/start_warehouse.html'


class StartConfiguration(TemplateView):
    template_name = 'configuration/start_configuration.html'


class StartSales(TemplateView):
    template_name = 'sales/start_sales.html'


class StartPurchases(TemplateView):
    template_name = 'purchases/start_purchases.html'


class StartAccounting(TemplateView):
    template_name = 'accounting/start_accounting.html'
