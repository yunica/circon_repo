from django import forms
from .models import AccountPlan


class Create(forms.ModelForm):

    class Meta:
        model = AccountPlan
        fields = ['code', 'description', 'active']

    def clean_accountplan(self):
        accountplan = self.cleaned_data.get('accountplan', '')
        if len(accountplan) < 0:
            raise forms.ValidationError("Ingrese por lo menos 1 letra")
        return accountplan
