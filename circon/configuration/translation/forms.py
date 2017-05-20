from django.forms import ModelForm
from django.contrib.auth.models import Permission


class CreateForm(ModelForm):

    class Meta:
        model = Permission
        fields = ['name']
