from django.shortcuts import render
from Quiz.models import Quiz # Import the model classes
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from django.contrib.auth.signals import user_logged_in
from django.http import HttpResponse
import requests

@csrf_exempt
def quiz(request):
	questions = Quiz.objects.all()
	context = {'questions':questions}
	return render(request, 'Quiz/quiz.html', context)

score=0

def answers(request):
	questions = Quiz.objects.all()
	global score
	for question in questions:
		correct_answer = question.answer 
		entered_answer = request.POST.get(str(question.id)) 
		if(entered_answer == correct_answer): 
			score+=1 

	context = {'score':score}
	return render(request, 'Quiz/answer.html', context)

def review(request):
	global score
	usr = User.objects.all()
	context = {'score':score,'usr':usr}
	return render(request, 'Quiz/review.html',context)


def certificate(request):
	global score
	context = {'score': score}
	return render(request, 'Quiz/certificate.html',context)


def check(request):
	adr=Quiz.objects.all()
	usr=User.objects.all()
	context = {'usr':usr,'adr':adr}
	return render(request, 'Quiz/check.html',context)

def studselect(request):
	return render(request, 'Quiz/studselect.html')

def leader(request):
	adr=Quiz.objects.all()
	usr=User.objects.all()
	context = {'usr':usr,'adr':adr}
	return render(request, 'Quiz/leader.html',context)