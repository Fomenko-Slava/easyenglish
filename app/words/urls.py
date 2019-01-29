from django.conf.urls import url

from . import views

# для использования в урлах, чтобы были уникальны words:word_list
app_name = 'words'

urlpatterns = [
    # ex: /words/
    url(r'^$', views.index, name='index'),
    # ex: /words/5/
    url(r'^(?P<id>\d+)/$', views.word_list, name='word_list'),

    # ex: /polls/5/results/
    #url(r'^(?P<question_id>[0-9]+)/results/$', views.results, name='results'),
    # ex: /polls/5/vote/
    #url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
]