from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.monsters, name='monsters'),
    url(r'^new', views.new, name='new')
]
