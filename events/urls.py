from django.conf.urls import patterns, url
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

urlpatterns = patterns('',
    url(r'home/$', 'events.views.events_home', name='events_home'),

    url(r'^$',
        lambda x: HttpResponseRedirect(reverse('events_home')),
        name='events_home_redirect'),

)