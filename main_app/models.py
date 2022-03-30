from distutils.command.upload import upload
from django.db import models
from django.urls import reverse

# Create your models here.
TIME = (
    ('M', 'Morning'),
    ('A', 'Afternoon' ),
    ('N', 'Night')
)

class Dog(models.Model):
    breed = models.CharField(max_length=200)
    description = models.TextField(max_length=250)
    activity = models.IntegerField()
    image = models.CharField(default=None, blank=True, null=True, max_length=255)

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