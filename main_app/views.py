from django.http import HttpResponse
from django.shortcuts import render
from .models import Dog

# Create your views here.

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def dog_breeds(request):
    dogs = Dog.objects.all()
    return render(request, 'dog/index.html', {'dogs': dogs})

def dogs_detail(request, dog_id):
    dog = Dog.objects.get(id=dog_id)
    return render(request, 'dog/detail.html', {'dog': dog})
