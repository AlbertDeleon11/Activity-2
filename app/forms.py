from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import UserProfile

class UserRegistrationForm(UserCreationForm):
    age = forms.IntegerField(required=False, widget=forms.NumberInput(attrs={'placeholder': 'Age'}))
    phone_number = forms.CharField(max_length=15, required=False, widget=forms.TextInput(attrs={'placeholder': 'Phone Number'}))
    year = forms.CharField(max_length=50, required=False, widget=forms.TextInput(attrs={'placeholder': 'Year'}))
    course = forms.CharField(max_length=100, required=False, widget=forms.TextInput(attrs={'placeholder': 'Course'}))

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'age', 'phone_number', 'year', 'course']

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['age', 'phone_number', 'year', 'course']
