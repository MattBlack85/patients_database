from django.contrib import admin

from visits_app.models import Visit
class VisitAdmin(admin.ModelAdmin):
    fields = ['patient','description']
    
admin.site.register(Visit, VisitAdmin)
