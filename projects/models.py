from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

from users.models import Employee_Profile

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
    project_Owner = models.ForeignKey(Employee_Profile, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return str(self.project_Code) + "-" + self.project_Name

class Questionaire(models.Model):
    """Model for adding questionaire"""
    question = models.TextField()
    related_Project = models.ForeignKey(Project, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.question[:80] + '...'

class ProjectMember(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    member = models.ForeignKey(Employee_Profile, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('project', 'member',)

    def __str__(self):
        return str(self.project.project_Code) + ' - ' + str(self.member.employee_i_d)