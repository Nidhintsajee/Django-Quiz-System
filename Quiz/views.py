from django.shortcuts import render
from Quiz.models import Quiz # Import the model classes
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
import requests

@csrf_exempt
def quiz(request):
	questions = Quiz.objects.all()
	context = {'questions':questions}
	return render(request, 'quiz.html', context)

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
	return render(request, 'answer.html', context)

def review(request):
	global score
	context = {'score':score}
	return render(request, 'review.html',context)


def certificate(request):
	global score
	context = {'score': score}
	return render(request, 'certificate.html',context)


def check(request):
	return render(request, 'check.html')

def studselect(request):
	return render(request, 'studselect.html')
