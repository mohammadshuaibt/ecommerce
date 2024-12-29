from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

class SignUpForm(UserCreationForm):
    email = forms.EmailField(
        required=True,
        help_text='Required. Please provide a valid email address.'
    )
    first_name = forms.CharField(
        max_length=100,
        required=True,
        help_text='Required. Please enter your first name.'
    )
    last_name = forms.CharField(
        max_length=100,
        required=True,
        help_text='Required. Please enter your last name.'
    )
    username = forms.CharField(
        max_length=50,
        required=True,
        help_text='Required. Please choose a username.'
    )
    password1 = forms.CharField(
        max_length=50,
        required=True,
        widget=forms.PasswordInput,
        help_text='Required. Minimum 8 characters.'
    )
    password2 = forms.CharField(
        max_length=50,
        required=True,
        widget=forms.PasswordInput,
        help_text='Required. Enter the same password as above.'
    )

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'password1', 'password2')

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise ValidationError("This email is already in use. Please choose another one.")
        return email

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise ValidationError("The two password fields didn't match.")
        return password2
    
class UpdateUserForm(UserChangeForm):
    email = forms.EmailField(
        required=True,
        help_text='Required. Please provide a valid email address.'
    )
    first_name = forms.CharField(
        max_length=100,
        required=True,
        help_text='Required. Please enter your first name.'
    )
    last_name = forms.CharField(
        max_length=100,
        required=True,
        help_text='Required. Please enter your last name.'
    )
    username = forms.CharField(
        max_length=50,
        required=True,
        help_text='Required. Please choose a username.'
    )