from django.db import models
from patients_app.models import Patient


class Visit(models.Model):
    patient = models.ForeignKey(Patient)
    date = models.DateField()
    description = models.TextField()
    
