from django.contrib import admin

from visits_app.models import Visit
Class VisitAdmin(admin.ModelAdmin):
    fields = ['description','patient']
admin.site.register(Visit, VisitAdmin)
