from django import forms

from .models import Project, ProjectMember, Questionaire

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = '__all__'

class QuestionaireForm(forms.ModelForm):
    class Meta:
        model = Questionaire
        fields = '__all__'

class ProjectMemberForm(forms.ModelForm):
    class Meta:
        model = ProjectMember
        fields = '__all__'