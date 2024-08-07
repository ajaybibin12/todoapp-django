from django import forms
from django.forms import ModelForm
from .models import Task

#create the model form

class TaskForm(forms.ModelForm):

    class Meta:
        model = Task
        fields = '__all__'


