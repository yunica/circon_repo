from django.views.generic import TemplateView
from django.views.generic import ListView
from django.views.generic import DetailView
from pure_pagination.mixins import PaginationMixin
from circon.warehouse.products.models import Products


class Index_View(PaginationMixin, ListView):
    template_name = 'website/home/index.html'
    model = Products
    paginate_by = 6


class ListProductsWeb(PaginationMixin, ListView):
    template_name = 'website/home/products.html'
    model = Products
    paginate_by = 9


class DetailProductsWeb(DetailView):
    template_name = 'website/home/detail.html'
    model = Products
    paginate_by = 1


class Contact(TemplateView):
    template_name = 'website/home/contact.html'


class Start_Login(TemplateView):
    template_name = 'website/home/index.html'
