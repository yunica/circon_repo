from django import forms
from circon.warehouse.units_measures.models import UnitsMeasures


class Create(forms.ModelForm):
    class Meta:
        model = UnitsMeasures
        fields = ['units_measures', 'active']

    def clean_units_measures(self):
        units_measures = self.cleaned_data.get('units_measures', '')
        if len(units_measures) < 0:
            raise forms.ValidationError("Ingrese por lomenos 1 letra")
        return units_measures
