from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here
class Feedback(models.Model):
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

    def __str__(self):
        return f"{self.email} - {self.get_category_display()}"









