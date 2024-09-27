
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserRegisterForm(UserCreationForm):
    password2 = forms.CharField(label= "confirm your password",widget=forms.PasswordInput)
    password = forms.CharField(label="password",widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ["email","username","password"]
    
    def clean_password2(self):
        password = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password and password2 and password2 != password:
            raise forms.ValidationError("Passwords do not match with each other!")
        return password
    
    
class UserLoginForm(forms.Form):
	username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
	password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))
