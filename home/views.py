
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required
from home.models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
import uuid
from home.forms import *
from django.db import transaction
from django import forms

# Home page view
def index(request):
    context = {
        'variable': "this is sent"
    }
    return render(request, "index.html", context)

def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        role = request.POST['role']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            auth_login(request, user)
            if role == "admin":
                return redirect('admindash')  # Replace with your admin dashboard URL
            elif role == "student":
                return redirect('student')  # Replace with your student dashboard URL
        else:
            messages.error(request, "Invalid username or password")
    return render(request, 'pages-login.html')


class SignUpForm(forms.ModelForm):
    password1 = forms.CharField(widget=forms.PasswordInput, label="Password")
    password2 = forms.CharField(widget=forms.PasswordInput, label="Confirm Password")

    class Meta:
        model = User
        fields = ['username', 'email']

    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get("password1")
        password2 = cleaned_data.get("password2")

        if password1 and password2 and password1 != password2:
            self.add_error('password2', "Passwords do not match")

        return cleaned_data


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        user_type = request.POST.get('user_type')

        if form.is_valid():
            with transaction.atomic():  # Ensure all operations are atomic
                # Create the User
                user = form.save(commit=False)
                user.set_password(form.cleaned_data['password1'])
                user.save()

                # Create role-specific profiles
                if user_type == 'student':
                    enrollment_number = request.POST.get('enrollment_number')
                    course = request.POST.get('course')
                    year_of_study = request.POST.get('year_of_study')

                    # Create the Student profile
                    Student.objects.create(
                        user=user,
                        enrollment_number=enrollment_number,
                        course=course,
                        year_of_study=year_of_study
                    )
                elif user_type == 'admin':
                    department = request.POST.get('department')

                    # Create the AdminProfile
                    AdminProfile.objects.create(
                        user=user,
                        department=department
                    )

                messages.success(request, "Your account has been created successfully.")
                return redirect('login')
        else:
            messages.error(request, "Please fix the errors below.")
    else:
        form = SignUpForm()

    return render(request, 'pages-signup.html', {'form': form})
# Logout view
def logout(request):
    auth_logout(request)
    return redirect('login')  # Redirect to the login page after logout

# Protected student view
@login_required(login_url='login')  # Require login to access this view
def student(request):
    if request.method == 'POST':
        category = request.POST.get('category')
        description = request.POST.get('description')

        # Create a new complaint entry
        Feedback.objects.create(
            user=request.user,
            category=category,
            description=description,
        )

        messages.success(request, "Your complaint has been registered successfully.")
        return redirect('student')

    # Fetch complaints of the logged-in user, including the complaint_id
    complaints = Feedback.objects.filter(user=request.user).order_by('timestamp')
    return render(request, 'student.html', {'complaints': complaints})


@login_required
def admindash(request):
    # Check if the user is an admin
    try:
        admin_profile = AdminProfile.objects.get(user=request.user)
    except AdminProfile.DoesNotExist:
        messages.error(request, "You are not authorized to view this page.")
        return redirect('home')

    # Fetch all complaints
    complaints = Feedback.objects.select_related('user').all().order_by('-timestamp')

    return render(request, 'admindash.html', {
        'complaints': complaints,
        'admin_profile': admin_profile
    })

@login_required
def update_complaint(request, complaint_id):
    complaint = Feedback.objects.get(complaint_id=complaint_id)

    if request.method == 'POST':
        # Update the complaint status and admin in charge
        complaint.status = request.POST.get('status')
        complaint.admin_in_charge = request.user.username
        complaint.save()

        # Create a new Remark
        Remark.objects.create(
            complaint=complaint,  # Associate the remark with the complaint
            admin=request.user,  # Assign the admin user to the remark
            remark=request.POST.get('remarks')  # Get the remark text from the form
        )

        return redirect('admindash')  # Redirect to the complaints list page

    return render(request, 'admindash.html', {'complaint': complaint})

def dashboard(request):
    # Fetch statistics
    issues_resolved = Complaint.objects.filter(status='resolved').count()
    complaints_received = Complaint.objects.count()
    pending_actions = Complaint.objects.filter(status='pending').count()
    no_of_users = User.objects.count()

    context = {
        'issues_resolved': issues_resolved,
        'complaints_received': complaints_received,
        'pending_actions': pending_actions,
        'no_of_users': no_of_users,
    }
    return render(request, 'index.html', context)


