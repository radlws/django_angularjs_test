from django.conf.urls import patterns, url

urlpatterns = patterns('',
    url(r'home/$', 'events.views.events_home', name='events_home'),

)