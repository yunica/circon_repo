from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.views.generic import ListView
from circon.warehouse.units_measures.models import UnitsMeasures
from django.views.generic.edit import CreateView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView
from django.core.urlresolvers import reverse
from django.core.urlresolvers import reverse_lazy
from pure_pagination.mixins import PaginationMixin
from .forms import Create


class ListUnitsMeasures(PaginationMixin, ListView):
    template_name = 'warehouse/units_measures/list.html'
    model = UnitsMeasures
    paginate_by = 10


class DetailUnitsMeasures(DetailView):
    template_name = 'warehouse/units_measures/detail.html'
    model = UnitsMeasures
    paginate_by = 1


class CreateUnitsMeasures(CreateView):
    form_class = Create
    initial = {'key': 'value'}
    template_name = 'warehouse/units_measures/create.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            units_measures = form.cleaned_data['units_measures']
            active = form.cleaned_data['active']
            p = UnitsMeasures()
            p.units_measures = units_measures
            p.active = active
            p.save()
            return HttpResponseRedirect('/List_UnitsMeasures')
        return render(request, self.template_name, {'form': form})


class UpdateUnitsMeasures(UpdateView):
    template_name = 'warehouse/units_measures/update.html'
    model = UnitsMeasures
    fields = ['units_measures', 'active']

    def get_success_url(self):
        return reverse('detail_units_measures', kwargs={'pk': self.object.pk})


class DeleteUnitsMeasures(DeleteView):
    template_name = 'warehouse/units_measures/delete.html'
    model = UnitsMeasures
    success_url = reverse_lazy('list_units_measures')
