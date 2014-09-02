from django.contrib import admin

from patients_app.models import Patient
from visits_app.models import Visit 

class VisitInline(admin.StackedInline): 
    model=Visit 
    extra=1 
    
class PatientAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Personal data',{'fields':['pesel']}),
                 (None,{'fields':['first_name','second_name','last_name']}),
                                      ]
    #list_display = ('name', 'pesel')#I don't like the look so I cancel it
    list_filter = ['last_name']
    search_fields=['last_name']
    inlines = [VisitInline]
    
admin.site.register(Patient,PatientAdmin)
