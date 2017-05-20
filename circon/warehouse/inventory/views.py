from django.views.generic import ListView
from django.views.generic import TemplateView
from django.views.generic.detail import SingleObjectMixin
from circon.warehouse.products.models import Products
from circon.warehouse.category.models import Category
from pure_pagination.mixins import PaginationMixin
from django.http import HttpResponse
from dal import autocomplete
from .forms import SearchForm
from django.views.generic.edit import FormMixin


class Inventory(PaginationMixin, FormMixin, ListView):
    template_name = 'warehouse/inventory/list.html'
    model = Products
    paginate_by = 10
    form_class = SearchForm

    def get_context_data(self, **kwargs):
        context = super(Inventory, self).get_context_data(**kwargs)
        context['category'] = Category.objects.all()
        context['form'] = self.get_form(self.form_class)
        return context


class SearchCategory(PaginationMixin, FormMixin, ListView):
    template_name = 'warehouse/inventory/list_category.html'
    model = Products
    paginate_by = 10
    form_class = SearchForm

    def get_queryset(self):
        pk = self.kwargs['pk']
        products = Products.objects.filter(category_id=pk)
        return products

    def get_context_data(self, **kwargs):
        context = super(SearchCategory, self).get_context_data(**kwargs)
        context['category'] = Category.objects.all()
        context['form'] = self.get_form(self.form_class)
        return context


class ProductsAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        if not self.request.user.is_authenticated():
            return Products.objects.none()
        qs = Products.objects.all()
        if self.q:
            qs = qs.filter(products__istartswith=self.q)
        return qs
