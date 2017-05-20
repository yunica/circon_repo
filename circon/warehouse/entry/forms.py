from circon.purchases.purchase.models import Purchase
from circon.purchases.purchase.models import PurchaseDetail
from django.forms import ModelForm
from django.forms.models import inlineformset_factory
from django import forms


class PurchaseForm(forms.ModelForm):

    class Meta:
        model = Purchase
        fields = '__all__'


class PurchaseDetailForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(PurchaseDetailForm, self).__init__(*args, **kwargs)
        instance = getattr(self, 'instance', None)
        if instance and instance.pk:
            self.fields['products'].widget.attrs['readonly'] = True

    def clean_products(self):
        instance = getattr(self, 'instance', None)
        if instance and instance.pk:
            return instance.products
        else:
            return self.cleaned_data['products']

    quan_purchase = forms.CharField(widget=forms.TextInput(attrs={'readonly':'readonly'}))

    class Meta:
        model = PurchaseDetail
        fields = '__all__'


PurchaseFormSet = inlineformset_factory(Purchase, PurchaseDetail, form=PurchaseDetailForm,
                                        extra=1)
