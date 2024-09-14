from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import aauthenticate
from account.models import Account
class RegistrationForm(UserCretionForm):
    email = forms.EmailField(max_lenght=60, help_text='Required. Add avalid email address')

    class Meta:
        model = Account
        fields = ("email", "username", "password1", "password2")

class AccountAuthenticationForm(forms.ModelForm):

    password = formms.Charfield(label='password', widget=forms.PasswordInput)

    class Meta:
        model = Account
        fields = ('email', 'password')

def clean(self):
    email = self.cleaned_data['email']
    password = self.cleaned_data['password']
    if not authenticated(email=email,password=password):
        raise forms.ValidationError("Invalid login") 