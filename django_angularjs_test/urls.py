from django.conf.urls import patterns, include, url
from django.contrib import admin
#from django.conf.urls.static import static
#from django.conf import settings

urlpatterns = patterns('',
    url(r'^verbatim/$', 'django_angularjs_test.views.test_verbatim', name='test_verbatim'),
    url(r'^interpolate/$', 'django_angularjs_test.views.test_interpolation', name='test_interpolation'),
    url(r'^controller/$', 'django_angularjs_test.views.test_controller', name='test_controller'),
    url(r'^events/', include('events.urls')),
    url(r'^admin/', include(admin.site.urls)),
) #+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
