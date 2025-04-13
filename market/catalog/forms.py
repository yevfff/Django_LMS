from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User


class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")


class LoginForm(forms.Form):
    username = forms.CharField(max_length=150)
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        fields = ("username", "password")


class ContactForm(forms.Form):
    name = forms.CharField(label='Ім’я', max_length=100)
    email = forms.EmailField(label='Email')
    subject = forms.CharField(label='Тема повідомлення', max_length=150)
    message = forms.CharField(label='Повідомлення', widget=forms.Textarea)
