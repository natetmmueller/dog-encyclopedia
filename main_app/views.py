from django.http import HttpResponse
from django.shortcuts import render
from .models import Dog
from django.views.generic.edit import CreateView

# Create your views here.

class DogCreate(CreateView):
    model = Dog
    fields = ['breed', 'description', 'activity', 'image']
    success_url = '/dogs'

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

