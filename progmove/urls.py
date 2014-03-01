#-*-encoding: -utf-8-*-

from django.conf.urls import patterns, include, url
import settings
from django.contrib import admin
admin.autodiscover()

from system.views import index

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'progmove.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', include('system.urls', namespace="system")),
	url(r'^admin/', include(admin.site.urls)),
)
