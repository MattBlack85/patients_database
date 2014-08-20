from django.db import models
from visits_app.models import Patient

# Create your models here.
class Visit(models.Model):
    patient = models.ForeignKey(Patient)
    date = models.DateField()
    description = models.TextField()
    
