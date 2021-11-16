from django.db import models
from django.conf import settings

# Create your models here.
class Employee_Profile(models.Model):
    employee_i_d = models.PositiveIntegerField()
    employee_name = models.CharField(max_length=100)
    employee_email = models.EmailField()
    employee_designation = models.CharField(max_length=100)
    employee_department = models.CharField(max_length=100)
    employee_location = models.CharField(max_length=50, choices=(('BLR1','Bangalore One'),
                                            ('BLR2','Bangalore Two'),
                                            ('GUR','Gurugram'),
                                            ('PUN','Pune'),
                                            ('KOC','Kochi')))
    is_lead = models.BooleanField(default=False)
    related_user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,)

    def __str__(self):
        return str(self.employee_i_d) + " : " + self.employee_name