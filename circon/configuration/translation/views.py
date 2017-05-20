from django.views.generic import ListView
from django.views.generic.edit import UpdateView
from .forms import CreateForm
from django.contrib.auth.models import Permission
from pure_pagination.mixins import PaginationMixin
from django.core.urlresolvers import reverse


class ListTranslationPermission(PaginationMixin, ListView):
    template_name = 'configuration/translation/permission/list.html'
    model = Permission
    paginate_by = 10


class UpdateTranslationPermission(UpdateView):
    template_name = 'configuration/translation/permission/update.html'
    model = Permission
    form_class = CreateForm

    def get_success_url(self):
        return reverse('list_translationpermission')
