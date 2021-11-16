from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
class Project(models.Model):
    """A model for projects"""
    project_Code = models.PositiveIntegerField()
    project_Name = models.CharField(max_length=100)
    date_Added = models.DateTimeField(auto_now_add=True)
    project_Description = models.TextField()
    project_Members_Allowed = models.PositiveIntegerField(default=5)
    project_Progress = models.IntegerField(
        default=0,
        validators=[MaxValueValidator(100), MinValueValidator(0)]
     )
    project_Closure = models.BooleanField(default=False)

    def __str__(self):
        return str(self.project_Code) + "-" + self.project_Name