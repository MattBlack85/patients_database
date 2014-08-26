from django.contrib import admin

from patients_app.models import Patient
class PatientAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Personal data',{'fields':['pesel']}),
                 (None,{'fields':['name']}),
                                      ]
    
admin.site.register(Patient,PatientAdmin)
