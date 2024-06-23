from django import forms
from .models import Sales

class SalesForm(forms.ModelForm):
    class Meta:
        model = Sales
        fields = ['PO_number', 'item_number', 'description', 'qnt', 'file']
