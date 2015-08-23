from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Newsletter(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    slug = models.SlugField(unique=True)
    
    #cover = models.ImageField(upload_to='newsletters')
    cover = models.CharField(max_length=127, default='DefaultCover.png')
    pdf = models.CharField(max_length=127, default='')

    def __str__(self):
        return self.name
