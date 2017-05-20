from .models import Purchase
from .models import PurchaseDetail
from django.forms import ModelForm
from django.forms.models import inlineformset_factory


class PurchaseForm(ModelForm):
    class Meta:
        model = Purchase
        fields = '__all__'


class PurchaseDetailForm(ModelForm):

    class Meta:
        model = PurchaseDetail
        fields = '__all__'


PurchaseFormSet = inlineformset_factory(Purchase, PurchaseDetail,
                                        form=PurchaseDetailForm, extra=1)
