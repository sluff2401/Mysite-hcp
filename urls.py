from django.conf.urls import patterns, include, url
from django.contrib import admin
from .                       import views
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/',                  include(admin.site.urls)),
    url(r'^accounts/login/$',        'django.contrib.auth.views.login'),
    url(r'^accounts/logout/$',       'django.contrib.auth.views.logout', {'next_page': '/'}),

    url(r'^siteadmindetail/$',       views.siteadmin_detail,                                  name='siteadmindetail'),
    url(r'^advertdisplay/$',         views.advert_display,                                    name='advertdisplay'),
    url(r'^advertinsert/$',          views.advert_insert,                                     name='advertinsert'),
    #url(r'^advertupdate/$',          views.advert_update,                                     name='advertupdate'),

    url(r''       ,                  include('events.urls')),
    url(r''       ,                  include('users.urls')),
)
