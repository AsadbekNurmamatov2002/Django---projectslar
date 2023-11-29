
from django import forms
from django.contrib.auth.models import User


class LoginForm(forms.Form):
    username=forms.CharField()
    password=forms.CharField(widget=forms.PasswordInput)

class UserRegistrForm(forms.ModelForm):
    password=forms.CharField(label='password', widget=forms.PasswordInput)
    password2=forms.CharField(label='password tekshiring', widget=forms.PasswordInput)
    class Meta:
        model=User
        fields=['username', 'first_name', 'email']

    def clean_password2(self):
        cd =self.changed_data
        if cd['password']!=cd['pasword2']:
           raise forms.ValidationError('Passwor o\'xshashemas!')
        return  cd['password2']