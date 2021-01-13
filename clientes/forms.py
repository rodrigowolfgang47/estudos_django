from django.contrib.auth.models import User
from django.forms import ModelForm
from .models import Person
from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.forms.widgets import PasswordInput, TextInput


class PersonForm(ModelForm):
    class Meta:
        model = Person
        fields = ['first_name', 'last_name', 'age', 'salary', 'bio', 'photo']

        labels = {'first_name': False, 'last_name': False, 'age': False, 'salary': False, 'bio': False, 'photo': False}
        
        widgets = {
            'first_name': forms.TextInput(attrs={'placeholder': 'Primeiro nome'}),
            'last_name': forms.TextInput(attrs={'placeholder': 'Ultimo nome'}),
            'age': forms.TextInput(attrs={'placeholder': 'Idade'}),
            'salary': forms.TextInput(attrs={'placeholder': 'Salário'}),
            'bio': forms.TextInput(attrs={'placeholder': 'Resumo'}),
            }

class MyAuthForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ['username','password']
    def __init__(self, *args, **kwargs):
        super(MyAuthForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget = forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Usuário'})
        self.fields['username'].label = False
        self.fields['password'].widget = forms.PasswordInput(attrs={'class': 'form-control', 'placeholder':'Senha'})
        self.fields['password'].label = False