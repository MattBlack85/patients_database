from django.db import models


class Patient(models.Model):
    name = models.CharField(max_length=200)
    pesel = models.IntegerField()
    pub_date = models.DateField(auto_now_add=True)
