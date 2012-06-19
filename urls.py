from django.conf.urls.defaults import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    
    url(r'^sina/authenticate', 'thirdlib.views.authenticate_handler'),
    url(r'^sina/callback', 'thirdlib.views.oauth_callback'),

    url(r'^qq/authenticate', 'thirdlib.views.authenticate_handler', {'third': 'QQ'}),
    url(r'^qq/callback', 'thirdlib.views.oauth_callback', {'third': 'QQ'}),
    
    url(r'^success', 'thirdlib.views.success'),
)
