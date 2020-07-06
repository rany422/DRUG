from django import forms
from .models import Drug_Master, Generic_Information
from datetime import date
from django.forms import ModelChoiceField



class ProductForm(forms.ModelForm):
    class Meta:
        model = Drug_Master
        fields= '__all__'

class Generic_InformationForm(forms.ModelForm):      
    class Meta:
        model=Generic_Information
        fields=['generic_name', 'generic_strength','generic_unit']
        

      