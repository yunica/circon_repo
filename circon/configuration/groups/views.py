from django.views.generic.detail import DetailView
from django.views.generic import ListView
from django.views.generic.edit import CreateView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView
from django.core.urlresolvers import reverse
from django.core.urlresolvers import reverse_lazy
from pure_pagination.mixins import PaginationMixin
from django.contrib.auth.models import Group
from .forms import CreateForm


class ListGroups(PaginationMixin, ListView):
    template_name = 'configuration/groups/list.html'
    model = Group
    paginate_by = 10


class DetailGroups(DetailView):
    template_name = 'configuration/groups/detail.html'
    model = Group
    paginate_by = 1


class CreateGroups(CreateView):

    form_class = CreateForm
    template_name = 'configuration/groups/create.html'
    success_url = reverse_lazy('list_groups')


class UpdateGroups(UpdateView):
    template_name = 'configuration/groups/update.html'
    model = Group
    form_class = CreateForm

    def get_success_url(self):
        return reverse('list_groups')


class DeleteGroups(DeleteView):
    template_name = 'configuration/groups/delete.html'
    model = Group
    success_url = reverse_lazy('list_groups')
