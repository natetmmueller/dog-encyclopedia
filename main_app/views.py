
from dataclasses import fields
from pydoc import classname
from urllib import request
from django.http import HttpResponse
from django.shortcuts import redirect, render
from .models import Dog, Toy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .forms import WalksForm
from django.views.generic import ListView, DetailView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

class DogCreate(CreateView):
    model = Dog
    fields = ['breed', 'description', 'activity', 'image']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def dog_breeds(request):
    dogs = Dog.objects.filter(user = request.user)
    return render(request, 'dog/index.html', {'dogs': dogs})

@login_required
def dogs_detail(request, dog_id):
    dog = Dog.objects.get(id=dog_id)
    toys_dog_doesnt_have = Toy.objects.exclude(id__in = dog.toys.all().values_list('id'))
    walks_form = WalksForm()
    return render(request, 'dog/detail.html', {'dog': dog, 'walks_form': walks_form, 'toys': toys_dog_doesnt_have})

@login_required
def add_walks(request, dog_id):
    form = WalksForm(request.POST)
    if form.is_valid():
        new_walks = form.save(commit=False)
        new_walks.dog_id = dog_id
        new_walks.save()
    return redirect('detail', dog_id = dog_id)

class DogUpdate(LoginRequiredMixin, UpdateView):
    model = Dog
    fields = ['breed', 'description', 'activity']

class DogDelete(LoginRequiredMixin, DeleteView):
    model = Dog
    success_url = '/dogs/'


class ToyList(LoginRequiredMixin, ListView):
    model = Toy


class ToyDetail(LoginRequiredMixin, DetailView):
    model = Toy

class ToyCreate(LoginRequiredMixin, CreateView):
    model = Toy
    fields = '__all__'

class ToyUpdate(LoginRequiredMixin, UpdateView):
    model = Toy
    fields = ['name', 'color']

class ToyDelete(LoginRequiredMixin, DeleteView):
    model = Toy
    success_url = '/toys/'

@login_required
def assoc_toy(request, dog_id, toy_id):
    Dog.objects.get(id = dog_id).toys.add(toy_id)
    return redirect('detail', dog_id = dog_id)

@login_required
def unassoc_toy(request, dog_id, toy_id):
    Dog.objects.get(id = dog_id).toys.remove(toy_id)
    return redirect('detail', dog_id = dog_id)

def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
        else:
            error_message = 'Invalid signup - try again'
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'registration/signup.html', context)