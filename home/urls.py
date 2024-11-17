from django.contrib import admin
from django.urls import path,include
from home import views

urlpatterns = [
    path('',views.index,name='index'),
    path('login/',views.login,name="login"),
    path('signup/', views.signup, name="signup"),
    # path('about',views.about,name='about'),
    # path('services',views.services,name='services'),
]
