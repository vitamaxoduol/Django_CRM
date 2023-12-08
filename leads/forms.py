from django import forms
from .models import Lead, Agent


class LeadModelForm(forms.ModelForm):
    agent = forms.ModelChoiceField(queryset=Agent.objects.all(), empty_label="Select Agent")
    class Meta:
        model = Lead
        fields = (
            'first_name',
            'last_name',
            'age',
            'agent'
        )
        
class LeadForm(forms.Form):
    first_name = forms.CharField()
    last_name = forms.CharField()
    age = forms.IntegerField(min_value=0)