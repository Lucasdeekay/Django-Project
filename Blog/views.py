from multiprocessing import context
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
import random, string
from Blog.models import BlogModel

random = random.Random()

# Create your views here.
def index(request):
    return render(request, "blog/index.html")

def result(request):
    email = request.POST.get("email")
    password = ""
    for i in range(12):
        character = random.choice(string.printable)
        if character != " ":
            password += character
    context = {'email': email, 'password': password}
    return render(request, "blog/result.html", context)


def generate_blogs(request):
    all_blogs = BlogModel.objects.all()
    context = {
        'all_blogs': all_blogs,
    }
    return render(request, 'blog/details.html', context)