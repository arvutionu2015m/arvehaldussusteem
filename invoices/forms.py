from django import forms
from .models import Invoice

class InvoiceForm(forms.ModelForm):
    tax_rate = forms.DecimalField(decimal_places=2)  # Veendu, et see on DecimalField

    class Meta:
        model = Invoice
        fields = ["client_name", "client_email", "amount", "currency", "tax_type", "tax_rate"]
