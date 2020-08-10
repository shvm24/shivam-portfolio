from django.shortcuts import render
from .models import Project

# Create your views here.
def aboutme(request):
    return render(request,'Home1/AboutMe.html')


def basic(request):
    Projects = Project.objects.all()
    return render(request,'Home1/basic.html', {'Projects':Projects})

def improvements(request):
    return render(request,'Home1/improvements.html')
    

def submit(request):
    return render(request,'Home1/submit.html')

