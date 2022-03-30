from django.http import HttpResponse
from django.shortcuts import redirect, render
from .models import Dog
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .forms import WalksForm

# Create your views here.

class DogCreate(CreateView):
    model = Dog
    fields = ['breed', 'description', 'activity', 'image']
    # success_url = '/dogs'

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def dog_breeds(request):
    dogs = Dog.objects.all()
    return render(request, 'dog/index.html', {'dogs': dogs})

def dogs_detail(request, dog_id):
    dog = Dog.objects.get(id=dog_id)
    walks_form = WalksForm()
    return render(request, 'dog/detail.html', {'dog': dog, 'walks_form': walks_form})

def add_walks(request, dog_id):
    form = WalksForm(request.POST)
    if form.is_valid():
        new_walks = form.save(commit=False)
        new_walks.dog_id = dog_id
        new_walks.save()
    return redirect('detail', dog_id = dog_id)

class DogUpdate(UpdateView):
    model = Dog
    fields = ['breed', 'description', 'activity']

class DogDelete(DeleteView):
    model = Dog
    success_url = '/dogs/'


