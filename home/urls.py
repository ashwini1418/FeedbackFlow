# from django.contrib import admin
# from django.urls import path,include
# from home import views
#
# urlpatterns = [
#
#
#     path('',views.index,name='index'),
#     path('login/',views.login,name="login"),
#     path('signup/', views.signup, name="signup"),
#
#     path('student/', views.student, name="student"),
#
#
#
#
# ]
from django.urls import path
from home import views

urlpatterns = [
    path('', views.index, name='index'),  # Home page view
    path('login/', views.login, name='login'),  # Login view
    path('signup/', views.signup, name='signup'),  # Signup view
    path('student/', views.student, name='student'),  # Protected student page
    path('logout/', views.logout, name='logout'),  # Logout view
    path('admindash/',views.admindash ,name='admindash'),
    path('admin/admindash/update/<str:complaint_id>/', views.update_complaint, name='update_complaint'),
]
