from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views.generic.detail import DetailView
from django.views.generic import ListView
from django.contrib.auth.models import User
from django.views.generic.edit import CreateView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView
from django.core.urlresolvers import reverse
from django.core.urlresolvers import reverse_lazy
from pure_pagination.mixins import PaginationMixin
from .forms import CreateForm
from .forms import ChangePasswordForm
from django.contrib.auth.hashers import make_password


class ListCustomers(PaginationMixin, ListView):
    template_name = 'sales/customers/list.html'
    model = User
    paginate_by = 10


class DetailCustomers(DetailView):
    template_name = 'sales/customers/detail.html'
    model = User
    paginate_by = 1


class CreateCustomers(CreateView):
    model = User
    form_class = CreateForm
    initial = {'key': 'value'}
    template_name = 'sales/customers/create.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            is_active = form.cleaned_data['is_active']
            company = form.cleaned_data['company']
            address = form.cleaned_data['address']
            phone = form.cleaned_data['phone']
            rif = form.cleaned_data['rif']
            provider = form.cleaned_data['provider']
            customers = form.cleaned_data['customers']
            p = User.objects.create_user(username=username,
                                         first_name=first_name,
                                         last_name=last_name,
                                         email=email, password=password,
                                         is_active=is_active,
                                         company=company, address=address,
                                         phone=phone, rif=rif,
                                         provider=provider,
                                         customers=customers)
            p.save()
            return HttpResponseRedirect('/List_Customers')

        return render(request, self.template_name, {'form': form})


class UpdateCustomers(UpdateView):
    template_name = 'sales/customers/update.html'
    model = User
    fields = ['username', 'first_name', 'last_name',
              'email', 'is_active', 'company', 'address', 'phone', 'rif',
              'provider', 'customers']

    def get_success_url(self):
        return reverse('detail_user', kwargs={'pk': self.object.pk})


class ChangePassword(UpdateView):
    template_name = 'sales/customers/password_change.html'
    form_class = ChangePasswordForm
    model = User
    fields = ['password']
    initial = {'key': 'value'}

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            user_id = User.objects.get(id=self.kwargs['pk'])
            user_id.password = make_password(form.cleaned_data['password'])
            user_id.save()
            return HttpResponseRedirect('/List_Customers')

        return render(request, self.template_name, {'form': form})


class DeleteCustomers(DeleteView):
    template_name = 'sales/customers/delete.html'
    model = User
    success_url = reverse_lazy('list_customers')
