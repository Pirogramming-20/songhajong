from django import forms
from .models import devTool

class devToolForm(forms.ModelForm):
    class Meta:
        model = devTool
        fields = ('__all__')