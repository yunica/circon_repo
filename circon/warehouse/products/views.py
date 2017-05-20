from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.views.generic import ListView
from circon.warehouse.products.models import Products
from django.views.generic.edit import CreateView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView
from django.core.urlresolvers import reverse
from django.core.urlresolvers import reverse_lazy
from pure_pagination.mixins import PaginationMixin
from .forms import Create
from braces.views import PermissionRequiredMixin


class ListProducts(PaginationMixin, ListView):
    template_name = 'warehouse/products/list.html'
    model = Products
    paginate_by = 10


class DetailProducts(DetailView):
    template_name = 'warehouse/products/detail.html'
    model = Products
    paginate_by = 1


class CreateProducts(PermissionRequiredMixin, CreateView):
    form_class = Create
    initial = {'key': 'value'}
    template_name = 'warehouse/products/create.html'
    permission_required = "products.add_products"
    login_url = '/'

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            products = form.cleaned_data['products']
            measure = form.cleaned_data['measure']
            description = form.cleaned_data['description']
            category = form.cleaned_data['category']
            image = form.cleaned_data['image']
            active   = form.cleaned_data['active']
            p = Products()
            p.products = products
            p.measure = measure
            p.quantity = '0'
            p.description = description
            p.category = category
            p.image = image
            p.active = active
            p.save()
            return HttpResponseRedirect('/List_Products')
        return render(request, self.template_name, {'form': form})


class UpdateProducts(UpdateView):
    template_name = 'warehouse/products/update.html'
    model = Products
    fields = ['products', 'measure', 'quantity', 'description',
              'category', 'image', 'active']

    def get_success_url(self):
        return reverse('detail_products', kwargs={'pk': self.object.pk})


class DeleteProducts(DeleteView):
    template_name = 'warehouse/products/delete.html'
    model = Products
    success_url = reverse_lazy('list_products')
