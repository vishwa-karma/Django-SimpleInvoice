from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

from .models import Invoice


class InvoiceForm(forms.ModelForm): 
    class Meta:
        model = Invoice
        fields = '__all__'
        invoice_date = forms.CharField()
        
        widgets={
                'invoice_date':forms.TextInput(attrs={"type": "date"})
                }
        

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.form_class = 'blueForms'
        self.helper.add_input(Submit('submit', 'Update Invoice'))
        
class InvoiceCreateForm(forms.ModelForm): 
    class Meta:
        model = Invoice
        fields = '__all__'
        invoice_date = forms.CharField()
        
        widgets={
                'invoice_date':forms.TextInput(attrs={"type": "date"})
                }
        

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.form_class = 'blueForms'
        self.helper.add_input(Submit('submit', 'Create Invoice'))