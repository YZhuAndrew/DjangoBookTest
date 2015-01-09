from django.conf import settings
from django.conf.urls import patterns, include, url
from django.contrib import admin
# from DjangoBookTest.views import hello
import DjangoBookTest.views
import contact.views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'DjangoBookTest.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^hello/$', DjangoBookTest.views.hello),
    url(r'^time/$', DjangoBookTest.views.current_datetime),
    url(r'^time/plus/(\d{1,2})/$', DjangoBookTest.views.hours_ahead),
    url(r'^meta/$', DjangoBookTest.views.display_meta),
    url(r'^meta2/$', DjangoBookTest.views.display_meta2),
    url(r'^search-form/$', DjangoBookTest.views.search),
    url(r'^search/$', DjangoBookTest.views.search),
    url(r'^search_results/$', DjangoBookTest.views.search),
    url(r'^get/$', DjangoBookTest.views.display_get),
    url(r'^contact/$', contact.views.contact),
    url(r'^post/$', 'DjangoBookTest.views.display_post'),
)

urlpatterns += patterns('contact.views',
    url(r'^contact/$', 'contact'),
)


if settings.DEBUG:
    urlpatterns += patterns('', (r'debuginfo/$', DjangoBookTest.views.debug))
