from django import forms
from circon.warehouse.products.models import Products


class Create(forms.ModelForm):
    class Meta:
        model = Products
        fields = ['products', 'measure', 'quantity', 'description', 'category',
                  'image', 'active']

    def clean_products(self):
        products = self.cleaned_data.get('products', '')
        if len(products) < 0:
            raise forms.ValidationError("Ingrese por lomenos 1 letra")
        return products
