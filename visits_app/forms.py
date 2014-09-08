from django import forms
from patients_app.models import Patient
from visits_app.models import Visit

class VisitForm(forms.ModelForm):
    class Meta:
        model = Visit
        exclude = ['date','patient']
        
