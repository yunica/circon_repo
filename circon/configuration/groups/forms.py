from django.forms import ModelForm
from django.contrib.auth.models import Group
from django.contrib.auth.models import Permission
from django.forms.widgets import CheckboxSelectMultiple


class CreateForm(ModelForm):
    class Meta:
        model = Group
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super(CreateForm, self).__init__(*args, **kwargs)
        self.fields["permissions"].widget = CheckboxSelectMultiple()
        self.fields["permissions"].queryset = Permission.objects.filter(content_type_id__in=[7, 12, 13, 14, 15, 16, 18, 20])
