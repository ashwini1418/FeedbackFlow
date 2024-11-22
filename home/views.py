
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required
from home.models import Feedback
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

# Home page view
def index(request):
    context = {
        'variable': "this is sent"
    }
    return render(request, "index.html", context)

# Login view
# def login(request):
#     if request.method == "POST":
#         username = request.POST.get('username')
#         password = request.POST.get('password')
#
#         # Authenticate the user
#         user = authenticate(request, username=username, password=password)
#         if user is not None:
#             auth_login(request, user)  # Log the user in
#             return redirect('student')  # Redirect to the student page
#         else:
#             return render(request, "pages-login.html", {"error": "Invalid username or password"})
#
#     return render(request, "pages-login.html")
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

# Signup view (optional, if you want to handle user registration)

# def signup(request):
#     if request.method == 'POST':
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             form.save()  # Save the new user to the database
#             messages.success(request, "Account created successfully. You can now log in.")
#             return redirect('login')  # Redirect to login page after successful registration
#         else:
#             messages.error(request, "Error creating account. Please check the form and try again.")
#     else:
#         form = UserCreationForm()
#
#     return render(request, 'pages-signup.html', {'form': form})

# def signup(request):
#     if request.method == 'POST':
#         username = request.POST['username']
#         email = request.POST['email']
#         password1 = request.POST['password1']
#         password2 = request.POST['password2']
#         user_type = request.POST['user_type']
#
#         if password1 != password2:
#             messages.error(request, "Passwords do not match.")
#             return redirect('signup')
#
#         user = UserCreationForm.objects.create_user(username=username, email=email, password=password1)
#         if user_type == 'admin':
#             user.is_staff = True  # Mark the user as admin
#         user.save()
#
#         messages.success(request, "Signup successful! You can now log in.")
#         return redirect('login')
#     return render(request, 'pages-signup.html')

def signup(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()  # This creates the user based on form data
            messages.success(request, 'Your account has been created successfully. You can now log in.')
            return redirect('login')  # Redirect to login after successful signup
        else:
            messages.error(request, 'There was an error with your signup. Please try again.')
    else:
        form = UserCreationForm()

    return render(request, 'pages-signup.html', {'form': form})
# Logout view
def logout(request):
    auth_logout(request)
    return redirect('login')  # Redirect to the login page after logout

# Protected student view
@login_required(login_url='login')  # Require login to access this view
def student(request):
    if request.method == "POST":
        email = request.POST.get('email')
        category = request.POST.get('category')
        description = request.POST.get('description')

        # Save feedback
        feedback = Feedback(email=email, category=category, description=description)
        feedback.save()

    return render(request, 'student.html')

