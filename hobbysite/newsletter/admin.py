from django.contrib import admin

from .models import Newsletter

class NewsletterAdmin(admin.ModelAdmin):
    pass
    
admin.site.register(Newsletter, NewsletterAdmin)