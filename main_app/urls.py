from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('dogs/', views.dog_breeds, name='index'),
    path('dogs/<int:dog_id>/', views.dogs_detail, name = 'detail'),
    path('dogs/create', views.DogCreate.as_view(), name='dogs_create'),
    path('dog/<int:pk>/update', views.DogUpdate.as_view(), name = 'dogs_update'),
    path('dog/<int:pk>/delete', views.DogDelete.as_view(), name = 'dogs_delete'),
    path('dogs/<int:dog_id>/add_walks', views.add_walks, name='add_walks')
]