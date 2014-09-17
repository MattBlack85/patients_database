from django.db import models

class Patient(models.Model):
    last_name = models.CharField(max_length=200)
    first_name = models.CharField(max_length=200)
    second_name = models.CharField(max_length=200, blank=True, null=True)
    pesel = models.CharField(max_length=11, blank=True, null=True)
    pub_date = models.DateField(auto_now_add=True)

    def __unicode__(self):
        if self.second_name:
            if self.pesel:
                return self.first_name + " " + self.second_name + " " + self.last_name + " " + str(self.pesel)
            else:
                return self.first_name + " " + self.second_name + " " + self.last_name
        else:
            if self.pesel:
                return self.first_name + " " + self.last_name + " " + str(self.pesel)
            else:
                return self.first_name + " " + self.last_name
