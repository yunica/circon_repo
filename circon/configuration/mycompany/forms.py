from django.forms import ModelForm
from circon.configuration.mycompany.models import MyCompany


class CreateForm(ModelForm):
    class Meta:
        model = MyCompany
        fields = "__all__"
