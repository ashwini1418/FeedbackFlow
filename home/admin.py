from django.contrib import admin
from home.models import complaint, Student, AdminProfile

#Register your model here.

admin.site.register(complaint)
admin.site.register(AdminProfile)
admin.site.register(Student)