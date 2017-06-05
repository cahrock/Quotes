from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^quotes$', views.quotes),
    url(r'^addquotes$', views.addquotes),
    url(r'^addfav/(?P<id>\d+)$', views.addfav),
    url(r'^removefav/(?P<id>\d+)$', views.removefav),
    url(r'^profile/(?P<id>\d+)$', views.profile),
    # url(r'^profile/(?P<posted_by>[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+)$', views.profile),
    url(r'^logout$', views.logout),
]
