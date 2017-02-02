from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.post_list, name = 'post_list'),
	# url(r'^blog/(?P<slug>[^\.])$', views.post_detail, name = 'post_detail'),
	url(r'^blog/view/(?P<slug>[^\.]+)', views.post_detail, name = 'post_detail'), 
]