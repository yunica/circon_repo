from django.http import HttpResponseRedirect
from django.views.generic.detail import SingleObjectMixin
from django.views.generic import ListView
from .models import Sale
from .models import SaleDetail
from django.views.generic.edit import CreateView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView
from django.core.urlresolvers import reverse
from django.core.urlresolvers import reverse_lazy
from pure_pagination.mixins import PaginationMixin
from .forms import SaleForm
from .forms import SaleFormSet
from .forms import SaleDetailForm
from extra_views import UpdateWithInlinesView
from extra_views import InlineFormSet
from circon.warehouse.products.models import Products


class ListSale(PaginationMixin, ListView):
    template_name = 'sales/sale/list.html'
    model = Sale
    paginate_by = 10
    ordering = '-pk'


class DetailSaleDetail(SingleObjectMixin, ListView):
    template_name = 'sales/sale/detail.html'
    paginate_by = 10

    def get(self, request, *args, **kwargs):
        self.object = self.get_object(queryset=Sale.objects.all())
        return super(DetailSaleDetail, self).get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(DetailSaleDetail, self).get_context_data(**kwargs)
        context['sale'] = self.object
        return context

    def get_queryset(self):
        return self.object.saledetail_set.all()


class CreateSale(CreateView):
    template_name = 'sales/sale/create.html'
    model = Sale
    form_class = SaleForm
    success_url = '/List_Sale'

    def get(self, request, *args, **kwargs):
        self.object = None
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        sale_form = SaleFormSet()
        return self.render_to_response(self.get_context_data(form=form,
                                       sale_form=sale_form,))

    def post(self, request, *args, **kwargs):
        self.object = None
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        sale_form = SaleFormSet(self.request.POST)
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
        return self.render_to_response(self.get_context_data(form=form,
                                       sale_form=sale_form,)
                                       )


class ItemInline(InlineFormSet):
    model = SaleDetail
    form_class = SaleDetailForm
    extra = 3


class UpdateSale(UpdateWithInlinesView):
    template_name = 'sales/sale/update.html'
    model = Sale
    inlines = [ItemInline]

    def get_success_url(self):
        return reverse('detail_sale', kwargs={'pk': self.object.pk})


class DeleteSale(DeleteView):
    template_name = 'sales/sale/delete.html'
    model = Sale
    success_url = reverse_lazy('list_sale')


class Confirm(UpdateView):
    template_name = 'sales/sale/confirm.html'
    model = Sale
    fields = ['status']
    initial = {'status': '1'}

    def get_success_url(self):
        id_products_sale = SaleDetail.objects.filter(relationship_id=self.object.pk)
        for x in id_products_sale:
            cant_products = Products.objects.filter(id=x.products_id)
            for z in cant_products:
                total = z.quantity - x.quantity
                update = Products.objects.values('quantity').filter(id=x.products_id).update(quantity=total)
        return reverse('detail_sale', kwargs={'pk': self.object.pk})


class Cancel(UpdateView):
    template_name = 'sales/sale/cancel.html'
    model = Sale
    fields = ['status']
    initial = {'status': '2'}

    def get_success_url(self):
        return reverse('detail_sale', kwargs={'pk': self.object.pk})
