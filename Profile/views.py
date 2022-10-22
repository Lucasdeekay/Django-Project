from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import logout
from .models import Profile

def index(request):
    return render(request, 'profile/index.html')

def details(request):
    if request.user.is_authenticated and not request.user.is_superuser:
        return render(request, "profile/details.html")
    else:
        return HttpResponseRedirect(reverse("Profile:register"))

def register(request):
    return render(request, "profile/register.html")

def reg_validate(request):
    first_name = request.POST.get('firstName').strip().capitalize()
    last_name = request.POST.get('lastName').strip().capitalize()
    username = request.POST.get('username').strip().capitalize()
    email = request.POST.get('email').strip().capitalize()
    gender = request.POST.get('gender').capitalize()
    password = request.POST.get('password').strip().capitalize()
    password2 = request.POST.get('password2').strip().capitalize()

    if username != "" and password != "":
        if password == password2:
            User.objects.create_user(username=username, password=password)
            Profile.objects.create(firstName=first_name, lastName=last_name, email=email, username=username, gender=gender)
            messages.success(request, "Registration successful")
            return HttpResponseRedirect(reverse('Profile:details'))
        else:
            messages.error(request, 'Password does not match')
            return HttpResponseRedirect(reverse('Profile:register'))
    else:
        messages.error(request, "Username or password cannot be empty")
        return HttpResponseRedirect(reverse('Profile:register'))

    
def log_out(request):
    logout(request)
    return HttpResponseRedirect(reverse('Profile:home'))
