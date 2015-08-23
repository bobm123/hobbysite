from django.conf.urls import include, url
from django.contrib import admin

from events import views as events_views
from events import urls as events_urls
from newsletter import urls as newsletter_urls 


urlpatterns = [
    # Examples:
    # url(r'^$', 'hobbysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', events_views.home_page, name='home'),
    url(r'^events', include(events_urls)),
    url(r'^maxfax', include(newsletter_urls)),
]
