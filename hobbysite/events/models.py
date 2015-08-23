from django.db import models


class Event(models.Model):
    date = models.DateField()
    name = models.CharField(max_length=60)
    location = models.CharField(max_length=60)
    contact_name = models.CharField(max_length=40)
    contact_email = models.EmailField(blank=True)
    contact_phone = models.CharField(max_length=12, blank=True)
    flyer = models.URLField()
    
    def __str__(self):
        return self.name
