from django.contrib import admin

from patients_app.models import Patient
from visits_app.models import Visit #trial

class VisitInline(admin.StackedInline): #trial
    model=Visit #trial
    extra=3 #trial
class PatientAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Personal data',{'fields':['pesel']}),
                 (None,{'fields':['name']}),
                                      ]
    
admin.site.register(Patient,PatientAdmin)
