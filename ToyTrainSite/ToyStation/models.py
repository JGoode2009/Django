from django.db import models

# Create your models here.
class Toy(models.Model):
    name=models.CharField(max_length=100)
    description = models.TextField(default='default')
    # photo = models.ImageField(upload_to='toys/photos/')