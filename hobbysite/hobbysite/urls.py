from django.conf.urls import include, url
from django.contrib import admin

from basicpage import views as basic_views
from hobbysite import views as hobbysite_views

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

    url(r'^accounts/login/$', hobbysite_views.login, name='login'),
    url(r'^accounts/auth/$', 'hobbysite.views.auth_view'),
    url(r'^accounts/logout/$', hobbysite_views.logout, name='logout'),
    url(r'^accounts/loggedin/$', 'hobbysite.views.loggedin'),
    url(r'^accounts/invalid/$', 'hobbysite.views.invalid_login'),

]
