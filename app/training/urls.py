from django.conf.urls import url

from . import views

urlpatterns = [

    url(r'^(?P<id>\d+)/$', views.word_list, name='word_list'),

]