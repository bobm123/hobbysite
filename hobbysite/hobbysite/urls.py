from django.conf.urls import include, url
from django.contrib import admin

from basicpage import views as basic_views
from events import urls as events_urls
from newsletter import urls as newsletter_urls 


urlpatterns = [
    # Examples:
    # url(r'^$', 'hobbysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', basic_views.home_page, name='home'),
    url(r'^about$', basic_views.about_page, name='about'),
    url(r'^anno$', basic_views.anno_page, name='anno'),
    url(r'^events', include(events_urls)),
    url(r'^maxfax', include(newsletter_urls)),
]
