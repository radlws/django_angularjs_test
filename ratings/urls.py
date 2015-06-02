from django.conf.urls import patterns, url

urlpatterns = patterns('',
    url(r'api/get$', 'ratings.views.ratings_api_get', name='ratings_api_get'),
    url(r'$', 'ratings.views.ratings_home', name='ratings_home'),

)