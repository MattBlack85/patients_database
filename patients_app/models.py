from django.db import models


class Patient(models.Model):
    name = models.CharField(max_length=200)
    first_name = models.CharField(max_length=200)
    second_name = models.CharField(max_length=200, blank=True, null=True)
    pesel = models.IntegerField(max_length=11, blank=True, null=True)
    pub_date = models.DateField(auto_now_add=True)

    def __unicode__(self):
        if second_name:
            return self.first_name + " " + self.second_name +" " + self.name + " (PESEL: " + str(self.pesel) + ")"
        else:
            return self.first_name + " " + self.name + " (PESEL: " + str(self.pesel) + ")"
