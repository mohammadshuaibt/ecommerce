from django import forms
from .models import Customer
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, SetPasswordForm
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
    password = None
    email = forms.EmailField(
        required=True,

    )
    first_name = forms.CharField(
        max_length=100,
        required=True,
    )
    last_name = forms.CharField(
        max_length=100,
        required=True,
    )
    username = forms.CharField(
        max_length=50,
        required=True,
    )

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name')

class UpdatePasswordForm(SetPasswordForm):
    new_password1 = forms.CharField(
        max_length=50,
        required=True,
        widget=forms.PasswordInput,
        label= "New Password"
    )
    new_password2 = forms.CharField(
        max_length=50,
        required=True,
        widget=forms.PasswordInput,
        label="Confirm Password"
    )

    class Meta:
        model= User
        fields = ('new_password1', 'new_password2')

class UpdateCustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['phone', 'address']
        widgets = {
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your phone number'}),
            'address': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter your address', 'rows': 3}),
        }