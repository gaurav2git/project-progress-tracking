from django import forms

from .models import Answer, Project, ProjectMember, Questionaire, Answer

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

class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = '__all__'