from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'joins.views.home', name='home'),
    # url(r'^testhome$', 'dmc.views.home', name='testhome'),
    # url(r'^blog/', include('blog.urls')),
)
