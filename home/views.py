
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required
from home.models import complaint,Student, AdminProfile
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
import uuid
from home.forms import *

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
                return redirect('admin')  # Replace with your admin dashboard URL
            elif role == "student":
                return redirect('student')  # Replace with your student dashboard URL
        else:
            messages.error(request, "Invalid username or password")
    return render(request, 'pages-login.html')



def signup(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            # Save the User
            user = form.save()

            # Determine role and save additional information
            role = form.cleaned_data['role']
            if role == 'student':
                Student.objects.create(
                    user=user,
                    enrollment_number=form.cleaned_data['enrollment_number'],
                    course=form.cleaned_data['course'],
                    year_of_study=form.cleaned_data['year_of_study'],
                )
            elif role == 'admin':
                AdminProfile.objects.create(
                    user=user,
                    department=form.cleaned_data['department'],
                )

            messages.success(request, 'Your account has been created successfully. You can now log in.')
            return redirect('login')  # Redirect to login after successful signup
        else:
            messages.error(request, 'There was an error with your signup. Please try again.')
    else:
        form = CustomUserCreationForm()

    return render(request, 'pages-signup.html', {'form': form})
# Logout view
def logout(request):
    auth_logout(request)
    return redirect('login')  # Redirect to the login page after logout

# Protected student view
@login_required(login_url='login')  # Require login to access this view
def student(request):
    if request.method == "POST":
        # Get category and description from the form
        category = request.POST.get('category')
        description = request.POST.get('description')

        # Automatically fetch the email from the logged-in user's profile
        email = request.user.email

        # Create a new complaint
        comp = complaint.objects.create(
            email=email,
            category=category,
            description=description,
        )

        # Provide a success message to the user
        return render(request, 'student.html', {'message': 'Complaint successfully registered.'})

    return render(request, 'student.html')

