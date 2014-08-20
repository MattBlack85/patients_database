from django.db import models

# Create your models here.
class Patient(models.Model):
    name = models.CharField(max_length=200)
    pesel = models.IntegerField()
    pub_date = models.DateField('patient added on: ')
