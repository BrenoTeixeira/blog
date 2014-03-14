from django.conf.urls import patterns, url

from .views import HomePageView

urlpatterns = patterns('core.views',
	url(r'^$', HomePageView.as_view(), name='home')	
)