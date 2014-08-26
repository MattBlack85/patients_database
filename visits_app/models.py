from django.db import models
from patients_app.models import Patient


class Visit(models.Model):
    patient = models.ForeignKey(Patient)
    date = models.DateField(auto_now_add=True)
    description = models.TextField()

    def __unicode__(self):
        return str(self.date)
