import uuid
from django.db import models
from django.contrib.auth.models import User




class Feedback(models.Model):
    complaint_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # ForeignKey to the User model
    category = models.CharField(max_length=100)
    description = models.TextField()
    status = models.CharField(max_length=20, default='Pending')  # Pending, In Progress, Resolved
    timestamp = models.DateTimeField(auto_now_add=True)  # Automatically set at creation

    def __str__(self):
        return f"{self.category} - {self.user.username}"  # Now 'self.user' will work correctly


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