import uuid
from django.db import models
from django.contrib.auth.models import User

class complaint(models.Model):
    CATEGORY_CHOICES = [
        ('student', 'Student'),
        ('staff', 'Staff'),
    ]

    email = models.EmailField(max_length=254)  # Using EmailField for proper email validation
    category = models.CharField(
        max_length=120,
        choices=CATEGORY_CHOICES,  # Dropdown options for the category
        default='student'  # Default value if not selected
    )
    description = models.TextField()  # Use TextField for longer descriptions
    feedback_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)  # UUID as a unique identifier
    timestamp = models.DateTimeField(auto_now_add=True)  # Auto-generate timestamp

    def __str__(self):
        return f"{self.feedback_id} - {self.get_category_display()}"



class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    enrollment_number = models.CharField(max_length=20, unique=True)
    course = models.CharField(max_length=100)
    year_of_study = models.PositiveIntegerField()

    def __str__(self):
        return f"Student: {self.user.username} - {self.enrollment_number}"


class AdminProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    department = models.CharField(max_length=100)

    def __str__(self):
        return f"Admin: {self.user.username} - {self.department}"