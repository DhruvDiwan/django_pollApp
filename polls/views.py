from django.shortcuts import render
from django.http import HttpResponse
from .models import Question

# Create your views here.
def index(request):
	latest_5_q = Question.objects.order_by('-pub_date')[:5]
	output = " , ".join(q.question_text for q in latest_5_q)
	return HttpResponse(output)

def detail(request , question_id):
	return HttpResponse("This is detail view of question %s" %question_id)

def results(request , question_id):
	return HttpResponse("These are the results of question %s" %question_id)

def vote(request , question_id):
	return HttpResponse("Vote on question %s" % question_id)