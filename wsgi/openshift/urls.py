from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    #url(r'^$', 'openshift.views.home', name='home'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^registro/$', 'openshift.LoLpossessions.views.registro'),
    url(r'^$', 'openshift.LoLpossessions.views.login'),
	url(r'^check/$', 'openshift.LoLpossessions.views.check'),
)
