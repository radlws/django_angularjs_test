from django.conf.urls import patterns, url

urlpatterns = patterns('',
    url(r'api$', 'ratings.views.ratings_api', name='ratings_api'),
    url(r'$', 'ratings.views.ratings_home', name='ratings_home'),

)