from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$' , views.index , name='index'),
	# 127.0.0.1/polls
	url(r'^(?P<question_id>[0-9]+)/$' , views.detail , name="detail"),
	#localhost/polls/2
	url(r'^(?P<question_id>[0-9]+)/results$' , views.results , name="results"),
	#localhost/polls/2/results
	url(r'^(?P<question_id>[0-9]+)/vote$' , views.vote , name="vote"),
	#localhost/polls2/vote
]