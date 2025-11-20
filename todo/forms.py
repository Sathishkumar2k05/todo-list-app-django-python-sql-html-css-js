from django import forms
from .models import Task

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title','description','completed']

        widgets = {
            'title':forms.TextInput(attrs={
                'class':"form-control",
                'style':'width:300px'
            }),
            'description':forms.Textarea(attrs={
                'style':'width:300px; height:300px; display:block; align-items:center; overflow-y:scroll; scrollbar-width:none;'
            }),
            'completed':forms.CheckboxInput(attrs={
                'class':'form-check-input',
                'style':'cursor:pointer;'
            })
        }