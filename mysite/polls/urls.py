from django.urls import path, re_path
from . import views

app_name = 'polls'

urlpatterns = [
    path('', views.index, name="index"),
    #127.0.0.1/polls/
    re_path('^(?P<question_id>[0-9]+)/$', views.details, name="detail"),
    #127.0.0.1/polls/2
    re_path('^(?P<question_id>[0-9]+)/results$', views.results, name="results"),
    #127.0.0.1/polls/2/results
    re_path('^(?P<question_id>[0-9]+)/vote$', views.vote, name="vote"),
    #127.0.0.1/polls/2/vote
]
