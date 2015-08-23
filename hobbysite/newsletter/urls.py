from django.conf.urls import url
from newsletter import views


urlpatterns = [
    url(r'^$', views.browse_by_year, name='browse_by_year'),
    url(r'^/(?P<year>[-\w]+)/$', views.browse_by_year, name='browse_by_year'),
]