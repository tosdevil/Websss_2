from .models import Task
from django.forms import ModelForm, TextInput

class TaskForm(ModelForm):

    class Meta:
        model = Task
        fields = ['TaskText']

        widgets = {
            "TaskText": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Задача'
            })
        }

