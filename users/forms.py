from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth import get_user_model




class RegistrationForm(UserCreationForm):
    email = forms.EmailField()
    username = forms.CharField(max_length=50)
   
    
    class Meta:
        model = get_user_model()
        fields = ['email', 'username', 'password1', 'password2']
        
        
        
class UpdateForm(UserChangeForm):
    
    class Meta:
        model = get_user_model()
        fields = []
        

    