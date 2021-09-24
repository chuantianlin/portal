from django import forms
from django.db.models import fields
from django.forms import widgets
from django.forms.fields import CharField
from .models import*

class NoteForm(forms.ModelForm):
    class Meta:
        model=Notes
        fields=['title','description']
class DateInput(forms.DateInput):
    input_type='date'

class HomeworkForm(forms.ModelForm):
    class Meta:
        model=Homework
        widgets={'due':DateInput()}
        fields=['subject','title','description','due','is_finished']
class Dashform(forms.Form):
        text=CharField(max_length=100,label="Enter your search")
class Todoform(forms.ModelForm):
    class Meta:
        model=Todo
        fields=['title','is_finished']
