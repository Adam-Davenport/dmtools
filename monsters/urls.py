from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.Monsters.as_view(), name='index'),
    url(r'^new$', views.MonsterCreate.as_view(), name='new')
]
