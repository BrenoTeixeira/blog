from django.conf.urls import patterns, url

from .views import HomePageView, PostListView

urlpatterns = patterns('core.views',
    url(r'^$', HomePageView.as_view(), name='home'),
    url(r'^blog/$', PostListView.as_view(), name='blog'),
)