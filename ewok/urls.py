from django.conf import settings
from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^$', 'exam.views.index', name='index'),
    url(r'^tests/$', 'exam.views.choose_test', name='choose-test'),
    url(r'^tests/(?P<test_id>\d+)/$', 'exam.views.start_test', name='start-test'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^redactor/', include('redactor.urls')),
)


if settings.DEBUG:
    urlpatterns += patterns(
        '',
        (
            r'^media/(?P<path>.*)$',
            'django.views.static.serve',
            {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}
        ),
    )