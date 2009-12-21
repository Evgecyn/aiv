
from django.conf.urls.defaults import patterns, include, handler500, handler404, url
from django.conf import settings
from django.contrib import admin
admin.autodiscover()

handler500 # Pyflakes

urlpatterns = patterns('')

if settings.DEBUG:
    pass

urlpatterns += patterns('', (r'^', include('config.urls')))    
urlpatterns += patterns('',
    (r'^media/(?P<path>.*)$', 'django.views.static.serve',
     {'document_root': settings.MEDIA_ROOT}),
)

urlpatterns += patterns(
    '',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('cms.urls')),
#    (r'^accounts/login/$', 'django.contrib.auth.views.login'),
)
