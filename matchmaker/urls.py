
from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin


urlpatterns = [
    # Examples:
    url(r'^$', 'dashboard.views.home', name='home'),
    url(r'^question/(?P<id>\d+)/$', 'questions.views.single', name='question_single'),
    url(r'^question/$', 'questions.views.home', name='question_home'),
    url(r'^contact/$', 'newsletter.views.contact', name='contact'),
    url(r'^about/$', 'matchmaker.views.about', name='about'),
    #url(r'^search/$', 'jobs.views.search', name='search'),
    url(r'^jobpost/$', 'jobpost.views.jobpost', name='job_post'),
    url(r'^jobapp/$', 'jobpost.views.jobapp', name='apply_job'),
    url(r'^jobview/$', 'jobpost.views.jobpostview', name='job_view'),
    #url(r'^search/', include('haystack.urls')),


    url(r'^like/(?P<id>\d+)/$', 'likes.views.like_user', name='like_user'),
    url(r'^profile/edit/$', 'profiles.views.profile_edit', name='profile_edit'),
    url(r'^profile/(?P<username>[\w.@+-]+)/$', 'profiles.views.profile_view', name='profile'),
    url(r'^profile/jobs/add/$', 'profiles.views.job_add', name='job_add'),
    url(r'^profile/jobs/edit/$', 'profiles.views.jobs_edit', name='jobs_edit'),
    url(r'^jobs/(?P<slug>[\w.@+-]+)/$', 'jobpost.views.individual_post', name='jobs'),
    url(r'^posts/$', 'jobpost.views.all_posts', name='posts'),



    url(r'^profile/$', 'profiles.views.profile_user', name='profile_user'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/', include('registration.backends.default.urls')),
    url(r'^matches/', include('matches.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)