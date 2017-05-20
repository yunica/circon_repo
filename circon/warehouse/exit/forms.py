from circon.warehouse.request.models import Request
from circon.warehouse.request.models import RequestDetail
from django.forms import ModelForm
from django.forms.models import inlineformset_factory
from django import forms


class RequestForm(forms.ModelForm):

    class Meta:
        model = Request
        fields = '__all__'


class RequestDetailForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(RequestDetailForm, self).__init__(*args, **kwargs)
        instance = getattr(self, 'instance', None)
        if instance and instance.pk:
            self.fields['products'].widget.attrs['readonly'] = True

    def clean_products(self):
        instance = getattr(self, 'instance', None)
        if instance and instance.pk:
            return instance.products
        else:
            return self.cleaned_data['products']

    quan_request = forms.CharField(widget=forms.TextInput(attrs={'readonly':'readonly'}))

    class Meta:
        model = RequestDetail
        fields = '__all__'


RequestFormSet = inlineformset_factory(Request, RequestDetail, form=RequestDetailForm,
                                       extra=1)
