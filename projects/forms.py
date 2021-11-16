from django import forms

from .models import Project, Questionaire

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = '__all__'

class QuestionaireForm(forms.ModelForm):
    class Meta:
        model = Questionaire
        fields = '__all__'