from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.views.generic import ListView
from circon.accounting.accountplan.models import AccountPlan
from django.views.generic.edit import CreateView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView
from django.core.urlresolvers import reverse
from django.core.urlresolvers import reverse_lazy
from pure_pagination.mixins import PaginationMixin
from .forms import Create


class ListAccountPlan(PaginationMixin, ListView):
    template_name = 'accounting/accountplan/list.html'
    model = AccountPlan
    paginate_by = 10


class DetailAccountPlan(DetailView):
    template_name = 'accounting/accountplan/detail.html'
    model = AccountPlan
    paginate_by = 1


class CreateAccountPlan(CreateView):
    form_class = Create
    initial = {'key': 'value'}
    template_name = 'accounting/accountplan/create.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            code = form.cleaned_data['code']
            description = form.cleaned_data['description']
            active = form.cleaned_data['active']
            p = AccountPlan()
            p.code = code
            p.description = description
            p.active = active
            p.save()
            return HttpResponseRedirect('/List_AccountPlan')

        return render(request, self.template_name, {'form': form})


class UpdateAccountPlan(UpdateView):
    template_name = 'accounting/accountplan/update.html'
    model = AccountPlan
    fields = ['code', 'description', 'active']

    def get_success_url(self):
        return reverse('detail_accountplan', kwargs={'pk': self.object.pk})


class DeleteAccountPlan(DeleteView):
    template_name = 'accounting/accountplan/delete.html'
    model = AccountPlan
    success_url = reverse_lazy('list_accountplan')
