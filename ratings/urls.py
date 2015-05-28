from django.conf.urls import patterns, url

urlpatterns = patterns('',
    url(r'$', 'ratings.views.ratings_home', name='ratings_home'),

)