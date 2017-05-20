from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views.generic.detail import DetailView
from django.views.generic import ListView
from django.views.generic.edit import CreateView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView
from django.core.urlresolvers import reverse
from django.core.urlresolvers import reverse_lazy
from pure_pagination.mixins import PaginationMixin
from .forms import CreateForm
from .models import MyCompany


class ListMyCompany(PaginationMixin, ListView):
    template_name = 'configuration/mycompany/list.html'
    model = MyCompany
    paginate_by = 10


class DetailMyCompany(DetailView):
    template_name = 'configuration/mycompany/detail.html'
    model = MyCompany
    paginate_by = 1


class CreateMyCompany(CreateView):
    form_class = CreateForm
    template_name = 'configuration/mycompany/create.html'
    success_url = reverse_lazy('list_mycompany')


class UpdateMyCompany(UpdateView):
    template_name = 'configuration/mycompany/update.html'
    model = MyCompany
    fields = "__all__"

    def get_success_url(self):
        return reverse('detail_user', kwargs={'pk': self.object.pk})


class DeleteMyCompany(DeleteView):
    template_name = 'configuration/mycompany/delete.html'
    model = MyCompany
    success_url = reverse_lazy('list_mycompany')
