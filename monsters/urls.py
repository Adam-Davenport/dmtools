from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.show)
    url(r'^new', views.new)
]
