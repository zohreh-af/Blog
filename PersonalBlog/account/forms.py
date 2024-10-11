

from django import forms
from django.core.exceptions import ValidationError

from .models import Profile


class UserRegisterForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}))
    password = forms.CharField(label='password', widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2 = forms.CharField(label='confirm password', widget=forms.PasswordInput(attrs={'class':'form-control'}))
    def clean(self) :
        cd = super().clean()
        p1 = cd.get('password')
        p2 = cd.get('password2')
        if p1 and p2 and p1 != p2 :
             raise ValidationError('passwords must match!')
          
    # def clean_password2(self):
    # password = self.cleaned_data.get('password1')
    # password2 = self.cleaned_data.get('password2')
    # if password and password2 and password2 != password:
    #     raise forms.ValidationError("Passwords do not match with each other!")
    #     return password
    
    
class UserLoginForm(forms.Form):
	username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
	password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))

class EditUserForm(forms.ModelForm):
    email = forms.EmailField(required=False)
    class Meta:
        model = Profile
        fields = ("age","bio")
