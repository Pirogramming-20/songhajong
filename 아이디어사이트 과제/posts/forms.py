from django import forms
from .models import IdeaItem

class IdeaForm(forms.ModelForm):
    class Meta:
        model = IdeaItem
        fields = ('__all__')