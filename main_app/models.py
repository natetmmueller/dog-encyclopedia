from distutils.command.upload import upload
from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.
TIME = (
    ('M', 'Morning'),
    ('A', 'Afternoon' ),
    ('N', 'Night')
)

class Toy(models.Model):
    name = models.CharField(max_length=50)
    color = models.CharField(max_length=20)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('toys_detail', kwargs={'pk': self.id})

class Dog(models.Model):
    breed = models.CharField(max_length=200)
    description = models.TextField(max_length=250)
    activity = models.IntegerField()
    image = models.CharField(default=None, blank=True, null=True, max_length=255)
    toys = models.ManyToManyField(Toy)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse('detail', kwargs = {'dog_id': self.id})
    
    def __str__(self):
        return self.breed



class Walks(models.Model):
    date = models.DateField()
    time = models.CharField(max_length=1, choices=TIME, default=TIME[0][0])
    dog = models.ForeignKey(Dog, on_delete = models.CASCADE)

    def __str__(self):
        return f'{self.get_time_display()} walk on {self.date}'

    class Meta:
        ordering = ['date']