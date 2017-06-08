from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.Monsters.as_view(), name='index'),
    url(r'^new$', views.MonsterCreate.as_view(), name='new'),
    url(r'^/(?P<pk>\d)$', views.MonsterDetails.as_view(), name='details'),
    url(r'^/(?P<pk>\d)/update$', views.MonsterUpdate.as_view(), name='update'),
    url(r'^/(?P<pk>\d)/delete$', views.MonsterDelete.as_view(), name='delete'),
]
