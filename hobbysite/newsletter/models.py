from django.contrib.auth.models import User
from django.db import models
from django.template.defaultfilters import slugify

# Create your models here.
class Newsletter(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    slug = models.SlugField(null=True, blank=True)
    
    #cover = models.ImageField(upload_to='newsletters')
    #cover = models.CharField(max_length=127, default='DefaultCover.png')
    #pdf = models.CharField(max_length=127, default='DefaultIssue.pdf')

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        #self.cover = self.slug+'.png'
        #self.pdf = self.slug+'.pdf'

        super(Newsletter, self).save(*args, **kwargs)

    @property
    def cover(self):
        return self.slug+'.png'
        
    @property
    def pdf(self):
        return self.slug+'.pdf'