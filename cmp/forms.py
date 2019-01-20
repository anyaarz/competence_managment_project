# -*-coding: utf-8 -*-
from django import forms
from .models import Employee,Job,Knowledge,Proficiency,Skills, User
from django.forms import inlineformset_factory

from django.contrib.auth.forms import UserCreationForm

class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repeat password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name' )

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Passwords don\'t match.')
        return cd['password2']


class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ('birth_date', 'avatar','is_active','job','education', 'department', 'location', 'date_applyied','date_retired','job_discription')
        help_texts = { 'location': ('Номер кабинета'), 'birth_date': ('Введите дату в формате: ГГГГ-ММ-ДД'),} 

class JobForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = ('name','is_active','discription','knowledge', 'proficiency','skills')


class KnowledgeForm(forms.ModelForm):
    class Meta:
        model = Knowledge
        fields = ('name','discription')
class ProficiencyForm(forms.ModelForm):
    class Meta:
        model = Proficiency
        fields = ('name','discription')

class SkillsForm(forms.ModelForm):
    class Meta:
        model = Skills
        fields = ('name','discription')

   
class LoginForm(forms.Form):

    """Форма для входа в систему
    """
    username = forms.CharField()
    password = forms.CharField()