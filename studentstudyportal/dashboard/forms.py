from django import forms
from django.db.models import fields
from django.forms import widgets
from django.forms.fields import CharField
from .models import*
from django.contrib.auth.forms import UserCreationForm

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


class coversionform(forms.Form):
    CHOICES=[('pound','Pound'),('kilogram','Kilogram')]
    measurement=forms.ChoiceField(choices=CHOICES,widget=forms.RadioSelect)


class CoversionLengthform (forms.Form):
        CHOICES=[('yard','Yard'),('foot','Foot')]
        input=forms.CharField(required=False,label=False,widget=forms.TextInput(
            attrs={'type':'number','placeholder':'Enter the number'} ))
        measure1=forms.CharField(
            label='',widget=forms.Select(choices=CHOICES)
        )
        measure1=forms.CharField(
            label='',widget=forms.Select(choices=CHOICES)
        )
class CoversionMASSform (forms.Form):
        CHOICES=[('pound','Pound'),('kilogram','kilogram')]
        input=forms.CharField(required=False,label=False,widget=forms.TextInput(
            attrs={'type':'number','placeholder':'Enter the number'}))
        measure1=forms.CharField(
            label='',widget=forms.Select(choices=CHOICES)
        )
        measure1=forms.CharField(
            label='',widget=forms.Select(choices=CHOICES)
        )


class UserRegisterForm(UserCreationForm):
        class Meta:
                model=User
                fields=['username','password1','password2']