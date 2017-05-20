from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.views.generic import ListView
from circon.warehouse.category.models import Category
from django.views.generic.edit import CreateView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView
from django.core.urlresolvers import reverse
from django.core.urlresolvers import reverse_lazy
from pure_pagination.mixins import PaginationMixin
from .forms import Create


class ListCategory(PaginationMixin, ListView):
    template_name = 'warehouse/category/list.html'
    model = Category
    paginate_by = 10


class DetailCategory(DetailView):
    template_name = 'warehouse/category/detail.html'
    model = Category
    paginate_by = 1


class CreateCategory(CreateView):
    form_class = Create
    initial = {'key': 'value'}
    template_name = 'warehouse/category/create.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            category = form.cleaned_data['category']
            active = form.cleaned_data['active']
            p = Category()
            p.category = category
            p.active = active
            p.save()
            return HttpResponseRedirect('/List_Category')

        return render(request, self.template_name, {'form': form})


class UpdateCategory(UpdateView):
    template_name = 'warehouse/category/update.html'
    model = Category
    fields = ['category', 'active']

    def get_success_url(self):
        return reverse('detail_category', kwargs={'pk': self.object.pk})


class DeleteCategory(DeleteView):
    template_name = 'warehouse/category/delete.html'
    model = Category
    success_url = reverse_lazy('list_category')
