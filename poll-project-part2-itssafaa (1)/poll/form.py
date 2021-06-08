from django import forms
from .models import Response,Option
class resform(forms.ModelForm):
  class Meta:
    model = Response
    
    fields ='__all__'
    options = forms.ModelChoiceField(queryset=Option.objects.all())
    
    
