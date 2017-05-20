from .models import Sale
from .models import SaleDetail
from django.forms import ModelForm
from django.forms.models import inlineformset_factory


class SaleForm(ModelForm):
    class Meta:
        model = Sale
        fields = '__all__'


class SaleDetailForm(ModelForm):

    class Meta:
        model = SaleDetail
        fields = '__all__'

SaleFormSet = inlineformset_factory(Sale, SaleDetail, form=SaleDetailForm,
                                    extra=1)
