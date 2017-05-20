from django import forms
from circon.warehouse.products.models import Products
from dal import autocomplete


class SearchForm(forms.ModelForm):
    products = forms.ModelChoiceField(
        queryset=Products.objects.all(),
        widget=autocomplete.ModelSelect2(url='products-autocomplete')
    )

    class Meta:
        model = Products
        fields = ('__all__')
