from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('dogs/', views.dog_breeds, name='index'),
    path('dogs/<int:dog_id>/', views.dogs_detail, name = 'detail')
]