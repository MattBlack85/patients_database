from django import forms
from patients_app.models import Patient


class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = ['first_name','second_name','last_name','pesel']
        
