from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.monsters)
    url(r'^new', views.new)
]
