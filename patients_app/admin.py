from django.contrib import admin

from patients_app.models import Patient
class PatientAdmin(admin.ModelAdmin):
    fields = ['pesel','name']
admin.site.register(Patient,PatientAdmin)
