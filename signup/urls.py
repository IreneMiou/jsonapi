from django.urls import re_path
from . import views

urlpatterns = [
    re_path(r'^$', views.signup, name='signup'),
    re_path(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,32})/$', views.activate, name='activate'),
]
