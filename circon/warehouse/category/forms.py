from django import forms
from circon.warehouse.category.models import Category


class Create(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['category', 'active']

    def clean_category(self):
        category = self.cleaned_data.get('category', '')
        if len(category) < 0:
            raise forms.ValidationError("Ingrese por lomenos 1 letra")

        return category
