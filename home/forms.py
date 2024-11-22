from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Student, AdminProfile


class CustomUserCreationForm(UserCreationForm):
    ROLE_CHOICES = [
        ('student', 'Student'),
        ('admin', 'Admin'),
    ]

    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'class': 'form-control'}))
    role = forms.ChoiceField(choices=ROLE_CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))

    # Fields for Student
    enrollment_number = forms.CharField(required=False, max_length=20,
                                        widget=forms.TextInput(attrs={'class': 'form-control'}))
    course = forms.CharField(required=False, max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    year_of_study = forms.IntegerField(required=False, widget=forms.NumberInput(attrs={'class': 'form-control'}))

    # Fields for Admin
    department = forms.CharField(required=False, max_length=100,
                                 widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'role', 'enrollment_number', 'course', 'year_of_study',
                  'department']
