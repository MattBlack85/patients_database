from django.db import models

# Create your models here.

class Patient(models.Model):
    name = models.CharField(max_length = 200)
    pesel = models.IntegerField()
    pub_date = models.DateTimeField('date added')

class Visit(models.Model):
    patient = models.ForeignKey(Patient)
    visit_date = models.DateTimeField('date of the visit')
    description = models.TextField()
    

    
