from .models import Request
from .models import RequestDetail
from django.forms import ModelForm
from django.forms.models import inlineformset_factory


class RequestForm(ModelForm):
    class Meta:
        model = Request
        fields = '__all__'


class RequestDetailForm(ModelForm):

    class Meta:
        model = RequestDetail
        fields = '__all__'

RequestFormSet = inlineformset_factory(Request, RequestDetail, form=RequestDetailForm,
                                       extra=1)
