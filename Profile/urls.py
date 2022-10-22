import imp
from django.urls import path
from Profile import views

app_name = "Profile"

urlpatterns = [
    path('', views.index, name="home"),
    path('details/', views.details, name="details"),
    path('register/', views.register, name="register"),
    path('register/validate/', views.reg_validate, name="reg_validate"),
    path('logout/', views.log_out, name="logout"),
]
