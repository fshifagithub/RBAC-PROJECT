from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from users.models import User

class RegistrationForm(UserCreationForm):#reg form have to create a us nd pass
    class Meta:
        model=User
        fields=["username","email","password1","password2"]

class LoginForm(forms.Form):   #inherit from forms

    username=forms.CharField()
    password=forms.CharField()

class UserProfileForm(forms.ModelForm):
    class Meta:
        model=User
        fields=["username","email","roles","is_active","permissions"]
        widgets={
            
            "username":forms.TextInput(attrs={"class":"form-control"}),
            "email":forms.TextInput(attrs={"class":"form-control"}),
            'roles': forms.TextInput(attrs={"class":"form-control"}),
            'permissions': forms.TextInput(attrs={"class":"form-control"}), 

        }
        

       


        