from django import forms
from .models import Resident, Municipal, Barangay
from leaflet.forms.widgets import LeafletWidget

from django.forms import DateInput

from django.forms.widgets import DateInput

class MyDateInput(DateInput):
    input_type = 'date'
    format = '%Y-%m-%d'

class ResidentAdminForm(forms.ModelForm):
    
    # birth_date = forms.DateField(widget=MyDateInput(attrs={'style': 'border-radius: 5px; border: 1px solid #ced4da;color: #495057;padding: 0.375rem 0.75rem;font-size: 1rem;','class':''}))
    
    
    class Meta:
        model = Resident
        fields = '__all__'
        
        
    def clean(self):
        cleaned_data = super().clean()
        barangay = cleaned_data.get("barangay")
        municipal = cleaned_data.get("municipal")
        if barangay and municipal:
            if barangay.municipal != municipal:
                raise forms.ValidationError("Barangay does not belong to selected municipal")
        return cleaned_data