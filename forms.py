from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    firstName = forms.Field(required=True)
    lastName = forms.Field(required=True)

    class Meta:
        model = User
        fields =[
            'username',
            'firstName',
            'lastName',
            'email',
            'password1',
            'password2'
            ]
    def save(self,commit=True):
     user = super(RegistrationForm,self).save(commit=False)
     user.firstName = self.cleaned_data['firstName']
     user.lastName = self.cleaned_data['lastName']
     user.email = self.cleaned_data['email']

     if commit:
         user.save()
     return user
    

