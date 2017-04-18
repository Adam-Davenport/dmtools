from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.encounters, name='Encounters')
]
