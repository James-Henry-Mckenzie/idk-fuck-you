from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import is_valid_path
from learn.static.math import Equation, fixe
from .forms import Answer
import random


def home(request):

    try:
        del request.session['new_q']
    except:
        pass
    try:
        del request.session['new_a']
    except:
        pass
    try:
        del request.session['user_answer']
    except:
        pass
    try:
        del request.session['points']
    except:
        pass
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')


def update_test(request):
    return render(request, 'update.html')

def question(request):
    form = Answer(request.POST)

    if not request.session.has_key('points'):
        request.session['points'] = 0


    if form.is_valid():
        user_answer = form.cleaned_data.get('aswer')
        request.session['user_answer'] = user_answer



    if request.session.has_key('user_answer'):
        question = str(request.session['new_q'])
        answer = str(request.session['new_a'])
        user_a = str(request.session['user_answer'])
        del request.session['user_answer']
        user_a2 = str(fixe(user_a))
        answer2 = str(fixe(answer))
        
        if user_a2 == answer or user_a2 == answer2 or user_a == answer or user_a == answer2:
            points = request.session['points']
            points += 1
            request.session['points'] = points
        points = request.session['points']
        return render(request, 'answer.html', {'b':question, 'ua':user_a, 'a':answer, 'ua2':user_a2, 'a2':answer2, 'points':points})
    else:
        
        # Get entire equation, answer and the question.
        equ = Equation(1, random.randint(-4, 4), 1, random.randint(-4, 4))
        equ.answer()

        answer = equ.answer
        question = equ.question

        points = request.session['points']

        request.session['new_q'] = question
        request.session['new_a'] = answer
        return render(request, 'question.html', {'Answer':answer, 'Question':question, 'form':form, 'points':points})
