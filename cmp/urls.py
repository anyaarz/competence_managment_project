from django.conf.urls import url
from . import views
#app_name = 'cmp'
urlpatterns = [
    url(r'^$', views.index, name = 'index'),
    url(r'^register/$', views.register, name='register'),
    #url(r'^edit/$', views.edit, name='edit'),
    url(r'^employees/$', views.EmployeesListView.as_view(), name = 'employees'),
    url(r'^employees/(?P<pk>\d+)/$', views.profile, name = 'profile'),
    url(r'^jobs/$', views.JobsListView.as_view(), name = 'jobs'),
    url(r'^competences/$', views.competences, name = 'competences'),
    #url(r'^competences/(?P<pk>\d+)$', views.KnowldgeDetailView.as_view(), name='knowledge-detail'),
    url(r'^post/new/$', views.post_new, name='post_new'),
    url(r'^post/(?P<pk>\d+)/edit/$', views.post_edit, name='post_edit'),
    url(r'^jobs/post/new/$', views.post_new_job, name='post_new_jobs'),
    url(r'^jobs/post/(?P<pk>\d+)/edit/$', views.post_edit_job, name='post_edit_jobs'),
    url(r'^competences/knowledge/post/new/$', views.post_new_k, name='post_new_k'),
    url(r'^competences/proficiency/post/new/$', views.post_new_p, name='post_new_p'),
    url(r'^competences/skills/post/new/$', views.post_new_s, name='post_new_s'),
    url(r'^competences/proficiency/post/(?P<pk>\d+)/edit/$', views.post_edit_p, name='post_edit_p'),
    
]


