from django.http import HttpResponseRedirect
from django.views.generic import ListView
from django.views.generic.detail import SingleObjectMixin
from .models import Request
from .models import RequestDetail
from django.views.generic.edit import CreateView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView
from django.core.urlresolvers import reverse
from django.core.urlresolvers import reverse_lazy
from pure_pagination.mixins import PaginationMixin
from .forms import RequestForm
from .forms import RequestFormSet
from .forms import RequestDetailForm
from extra_views import UpdateWithInlinesView
from extra_views import InlineFormSet


class ListRequest(PaginationMixin, ListView):
    template_name = 'warehouse/request/list.html'
    model = Request
    paginate_by = 10
    ordering = '-pk'


class DetailRequestDetail(PaginationMixin, SingleObjectMixin, ListView):
    template_name = 'warehouse/request/detail.html'
    paginate_by = 10

    def get(self, request, *args, **kwargs):
        self.object = self.get_object(queryset=Request.objects.all())
        return super(DetailRequestDetail, self).get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(DetailRequestDetail, self).get_context_data(**kwargs)
        context['sale'] = self.object
        return context

    def get_queryset(self):
        return self.object.requestdetail_set.all()


class CreateRequest(CreateView):
    template_name = 'warehouse/request/create.html'
    model = Request
    form_class = RequestForm
    success_url = '/List_Request'

    def get(self, request, *args, **kwargs):
        self.object = None
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        sale_form = RequestFormSet()
        return self.render_to_response(
               self.get_context_data(form=form,
                                     sale_form=sale_form,))

    def post(self, request, *args, **kwargs):
        self.object = None
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        sale_form = RequestFormSet(self.request.POST)
        if (form.is_valid() and sale_form.is_valid()):
            return self.form_valid(form, sale_form)
        else:
            return self.form_invalid(form, sale_form)

    def form_valid(self, form, sale_form):
        self.object = form.save(commit=False)
        self.object.applicant = self.request.user
        self.object.status = '0'
        self.object = form.save()
        sale_form.instance = self.object
        sale_form.save()
        return HttpResponseRedirect(self.get_success_url())

    def form_invalid(self, form, sale_form):
        return self.render_to_response(
               self.get_context_data(form=form,
                                     sale_form=sale_form,))


class ItemInline(InlineFormSet):
    model = RequestDetail
    form_class = RequestDetailForm
    extra = 3


class UpdateRequest(UpdateWithInlinesView):
    template_name = 'warehouse/request/update.html'
    model = Request
    inlines = [ItemInline]

    def get_success_url(self):
        return reverse('detail_request', kwargs={'pk': self.object.pk})


class DeleteRequest(DeleteView):
    template_name = 'warehouse/request/delete.html'
    model = Request
    success_url = reverse_lazy('list_request')


class Confirm(UpdateView):
    template_name = 'warehouse/request/confirm.html'
    model = Request
    fields = ['status']
    initial = {'status': '1'}

    def get_success_url(self):
        return reverse('detail_request', kwargs={'pk': self.object.pk})


class Delivered(UpdateView):
    template_name = 'warehouse/request/delivered.html'
    model = Request
    fields = ['status']
    initial = {'status': '2'}

    def get_success_url(self):
        return reverse('detail_request', kwargs={'pk': self.object.pk})


class Cancel(UpdateView):
    template_name = 'warehouse/request/cancel.html'
    model = Request
    fields = ['status']
    initial = {'status': '3'}

    def get_success_url(self):
        return reverse('detail_request', kwargs={'pk': self.object.pk})
