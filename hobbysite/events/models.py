from django.db import models


class Event(models.Model):
    date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    name = models.CharField(max_length=80)
    location = models.CharField(max_length=80)
    contact_name = models.CharField(max_length=40)
    contact_email = models.EmailField(blank=True)
    contact_phone = models.CharField(max_length=12, blank=True)
    flyer = models.URLField(blank=True)
    
    def __str__(self):
        return self.name
