from django.conf import settings
from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
                       url(r'^$', 'exam.views.index', name='index'),
                       # student register
                       url(r'^register$', 'exam.views.register', name='register'),
                       # teacher register
                       url(r'^signup$', 'exam.views.signup', name='signup'),
                       url(r'^results/view/(?P<result_id>\d+)$/?', 'exam.views.results', name='results'),
                       url(r'^tests/$', 'exam.views.choose_test', name='choose-test'),
                       url(r'^tests/(?P<test_id>\d+)/$', 'exam.views.start_test', name='start-test'),
                       #teacher login
                       #teacher dashboard
                       url(r'^logout$', 'exam.views.logout', name='logout'),
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
