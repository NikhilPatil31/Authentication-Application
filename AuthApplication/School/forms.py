from django import forms
from .models import User

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username','password']
        widgets = {
            'password':forms.PasswordInput
        }

class RegistrationForm(forms.Form):
    username = forms.CharField(max_length=20)   
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)

    def checkpass(self):
        password = self.cleaned_data.get('password')
        confirm_password = self.cleaned_data.get('confirm_password')

        if password and confirm_password and password != confirm_password:
            raise forms.ValidationError("Passwords do not match.")
        
        else:
            return password

    # class Meta:
    #     model = User
    #     fields = ['username','password','confirm_password']
    #     widgets = {
    #         'password':forms.PasswordInput,
    #         'confirm_password':forms.PasswordInput
    #     }