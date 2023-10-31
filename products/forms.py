from django import forms
from .models import Product

#this takes standard django form
class RawProductForm(forms.Form):
    title = forms.CharField(required=False)
    description = forms.CharField()
    price = forms.DecimalField()
    
#this takes model form
class ProductForm(forms.ModelForm):
        class Meta:
            model = Product
            fields = [
                 'title', 
                 'description',
                 'price']

