from django.db import models

# Create your models here.
class Project(models.Model):
    """A model for projects"""
    projectCode = models.PositiveIntegerField()
    projectName = models.CharField(max_length=100)
    date_added = models.DateTimeField(auto_now_add=True)
    projectDescription = models.TextField()
    projectMembersAllowed = models.PositiveIntegerField(default=5)

    def __str__(self):
        return str(self.projectCode) + "-" + self.projectName