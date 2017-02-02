from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.results_list, name = 'results_list'),
]