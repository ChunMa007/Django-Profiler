from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import User_Record
from django.contrib.auth.models import User

class SignUpUser(UserCreationForm):
    username = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder": "username", "class": "form-control"}), label="")
    first_name = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder": "first name", "class": "form-control"}), label="")
    last_name = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder": "last name", "class": "form-control"}), label="")
    email = forms.EmailField(required=True, widget=forms.widgets.EmailInput(attrs={"placeholder": "email", "class": "form-control"}), label="")
    
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'password1', 'password2')
    
    def __init__(self, *args, **kwargs):
        super(SignUpUser, self).__init__(*args, **kwargs)
        
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['placeholder'] = 'Password'
        self.fields['password1'].label = ''
        self.fields['password1'].help_text = '<ul class="form-text text-muted small"><li>Your password can\'t be too similar to your other personal information.</li><li>Your password must contain at least 8 characters.</li><li>Your password can\'t be a commonly used password.</li><li>Your password can\'t be entirely numeric.</li></ul>'

        self.fields['password2'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['placeholder'] = 'Confirm Password'
        self.fields['password2'].label = ''
        self.fields['password2'].help_text = '<span class="form-text text-muted"><small>Enter the same password as before, for verification.</small></span>'
    
class CreateProfile(forms.ModelForm):
    username = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder": "Username", "class": "form-control"}), label="")
    first_name = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder": "First Name", "class": "form-control"}), label="")
    last_name = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder": "Last Name", "class": "form-control"}), label="")
    email = forms.EmailField(required=True, widget=forms.widgets.EmailInput(attrs={"placeholder": "Email", "class": "form-control"}), label="")
    
    GENDER_CHOICES = [
        ("M", "Male"),
        ("F", "Female"),
    ]
    
    gender = forms.ChoiceField(choices=GENDER_CHOICES, required=True, widget=forms.Select(attrs={"class": "form-control"}), label="")
    image = forms.ImageField(required=False, widget=forms.FileInput(attrs={"class": "form-control"}), label="Profile Picture")
    
    class Meta:
        model = User_Record
        fields = ('username', 'first_name', 'last_name', 'email', 'gender', 'image')
    
