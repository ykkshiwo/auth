from django.conf.urls import url
from . import views


app_name = "app1"
urlpatterns = [
    url(r'^regist', views.regist_, name='regist'),
    url(r'^login', views.login_, name='login'),
    url(r'^a_y_l', views.are_you_login, name='are_you_login'),
    url(r'^logout', views.logout_, name='logout'),
]