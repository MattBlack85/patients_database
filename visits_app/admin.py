from django.contrib import admin

from visits_app.models import Visit
class VisitAdmin(admin.ModelAdmin):
    fields = ['patient','description']
    list_display = ('description')
    list_filter = ['date']
    
#admin.site.register(Visit, VisitAdmin)
#removed to display visits with patients, not separately
