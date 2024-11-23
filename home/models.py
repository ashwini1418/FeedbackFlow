import uuid
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Feedback(models.Model):
    complaint_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # The complainant
    category = models.CharField(max_length=100)
    description = models.TextField()
    status = models.CharField(max_length=20, default='Pending')  # Pending, In Progress, Resolved
    admin_in_charge = models.CharField(max_length=100, null=True, blank=True)  # Optional field for admin tracking
    remarks = models.TextField(null=True, blank=True)  # Internal remarks
    timestamp = models.DateTimeField(auto_now_add=True)  # Automatically set at creation

    def __str__(self):
        return f"{self.category} - {self.user.username}"  # Display the username as the complainant

class Remark(models.Model):
    complaint = models.ForeignKey('Feedback', on_delete=models.CASCADE, related_name='remarks_history')  # Use a unique related_name
    admin = models.ForeignKey(User, on_delete=models.CASCADE)
    remark = models.TextField()
    timestamp = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"Remark by {self.admin.username} on {self.timestamp}"


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