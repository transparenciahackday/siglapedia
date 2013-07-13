from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView
from acronyms import views

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', TemplateView.as_view(template_name="index.html"), name='home'),
    url(r'^pesquisa/', views.fetch, name='fetch'),
    url(r'^adicionar/', views.add, name='add'),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
)
