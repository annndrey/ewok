from django.conf import settings
from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.contrib.auth import views as auth_views

urlpatterns = patterns('',
                       url(r'^$', 'exam.views.index', name='index'),
                       # student register
                       url(r'^register$', 'exam.views.register', name='register'),
                       # accept personal data processing
                       url(r'^accept$', 'exam.views.personal_data_acceptance', name='accept'),
                       # teacher register
                       url(r'^signup$', 'exam.views.signup', name='signup'),
                       url(r'^results/view/(?P<result_id>\d+)$/?', 'exam.views.results', name='results'),
                       url(r'^tests/$', 'exam.views.choose_test', name='choose-test'),
                       url(r'^tests/(?P<test_id>\d+)/$', 'exam.views.start_test', name='start-test'),
                       #teacher login
                       #url(r'^login$', 'django.contrib.auth.views.login', {'template_name':'exam/login.html'}, name='login'),
                       url(r'^login$', 'exam.views.custom_login', name='login'),
                       #teacher account
                       url(r'^myaccount/$', 'exam.views.myaccount', name='myaccount'),
                       url(r'^logout$', 'exam.views.logout_view', name='logout'),
                       url(r'^admin/', include(admin.site.urls)),
                       url(r'^redactor/', include('redactor.urls')),
                       # for register form ajax queries
                       url(r'^a/get/teacher/?$', 'exam.views.get_teachers', name='get_teachers'),
                       url(r'^a/get/group/?$', 'exam.views.get_groups', name='get_groups'),
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
