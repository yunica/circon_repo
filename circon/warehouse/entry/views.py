from django.http import HttpResponseRedirect
from django.views.generic.detail import SingleObjectMixin
from django.views.generic import ListView
from circon.purchases.purchase.models import Purchase
from circon.purchases.purchase.models import PurchaseDetail
from django.views.generic.edit import CreateView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView
from django.core.urlresolvers import reverse
from django.core.urlresolvers import reverse_lazy
from pure_pagination.mixins import PaginationMixin
from .forms import PurchaseForm
from .forms import PurchaseFormSet
from .forms import PurchaseDetailForm
from extra_views import UpdateWithInlinesView, InlineFormSet
from circon.warehouse.products.models import Products


class ListEntry(PaginationMixin, ListView):
    template_name = 'warehouse/entry/list.html'
    model = Purchase
    paginate_by = 10
    ordering = '-pk'


class DetailEntryDetail(SingleObjectMixin, ListView):
    template_name = 'warehouse/entry/detail.html'
    paginate_by = 10

    def get(self, request, *args, **kwargs):
        self.object = self.get_object(queryset=Purchase.objects.all())
        return super(DetailEntryDetail, self).get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(DetailEntryDetail, self).get_context_data(**kwargs)
        context['purchase'] = self.object
        return context

    def get_queryset(self):
        return self.object.purchasedetail_set.all()


class CreateEntry(CreateView):
    template_name = 'warehouse/entry/create.html'
    model = Purchase
    form_class = PurchaseForm
    success_url = '/List_Entry'

    def get(self, request, *args, **kwargs):
        self.object = None
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        purchase_form = PurchaseFormSet()
        return self.render_to_response(
               self.get_context_data(form=form,
                                     purchase_form=purchase_form,))

    def post(self, request, *args, **kwargs):
        self.object = None
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        purchase_form = PurchaseFormSet(self.request.POST)
        if (form.is_valid() and purchase_form.is_valid()):
            return self.form_valid(form, purchase_form)
        else:
            return self.form_invalid(form, purchase_form)

    def form_valid(self, form, purchase_form):
        self.object = form.save(commit=False)
        self.object.applicant = self.request.user
        self.object.status = '0'
        self.object = form.save()
        purchase_form.instance = self.object
        purchase_form.save()
        return HttpResponseRedirect(self.get_success_url())

    def form_invalid(self, form, purchase_form):
        return self.render_to_response(
               self.get_context_data(form=form,
                                     purchase_form=purchase_form,))


class ItemInline(InlineFormSet):
    model = PurchaseDetail
    form_class = PurchaseDetailForm
    extra = 0


class UpdateEntry(UpdateWithInlinesView):
    template_name = 'warehouse/entry/update.html'
    model = Purchase
    inlines = [ItemInline]

    def get_success_url(self):
        return reverse('detail_entry', kwargs={'pk': self.object.pk})


class DeleteEntry(DeleteView):
    template_name = 'warehouse/entry/delete.html'
    model = Purchase
    success_url = reverse_lazy('list_entry')


class Confirm(UpdateView):
    template_name = 'warehouse/entry/confirm.html'
    model = Purchase
    fields = ['status']
    initial = {'status': '1'}

    def get_success_url(self):
        return reverse('detail_entry', kwargs={'pk': self.object.pk})


class Received(UpdateView):
    template_name = 'warehouse/entry/received.html'
    model = Purchase
    fields = ['status']
    initial = {'status': '2'}

    def get_success_url(self):
        id_products_detail = PurchaseDetail.objects.filter(relationship_id=self.object.pk)
        for x in id_products_detail:
            cant_products = Products.objects.filter(id=x.products_id)
            for z in cant_products:
                total = z.quantity + x.quantity
                update = Products.objects.values('quantity').filter(id=x.products_id).update(quantity=total)
        return reverse('detail_entry', kwargs={'pk': self.object.pk})


class Cancel(UpdateView):
    template_name = 'warehouse/entry/cancel.html'
    model = Purchase
    fields = ['status']
    initial = {'status': '3'}

    def get_success_url(self):
        return reverse('detail_entry', kwargs={'pk': self.object.pk})
