from django.db import models


class Patient(models.Model):
    name = models.CharField(max_length=200)
    pesel = models.IntegerField(max_length=11)
    pub_date = models.DateField(auto_now_add=True)

    def __unicode__(self):
        return self.name, self.pesel
