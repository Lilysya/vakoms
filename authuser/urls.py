from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$', views.activate, name='activate'),
    url(r'^logout/$', views.logout_view, name='logout'),
    url(r'^login/$', views.login_user, name='login'),
    url(r'^signup/$', views.signup, name='signup'),

]