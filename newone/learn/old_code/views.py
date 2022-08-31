from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import is_valid_path
from learn.static.math import Equation, fixe
from .forms import Answer
import random

# Create your views here.


def home(request):

    try:
        del request.session['question']
    except:
        pass
    try:
        del request.session['answer']
    except:
        pass
    try:
        del request.session['u_answer']
    except:
        pass
    return render(request, 'home.html')

def about(request):
    if request.session.has_key('question'):
        question = request.session['question']
        return render(request, 'about_question.html', {'Question':question})
    else:
        return render(request, 'question.html')

# def answer(request):
#     if request.session.has_key('u_answer'):
#         question = request.session['question']
#         answer = request.session['answer']
#         u_answer = request.session['u_answer']
#         return render(request, 'answer.html', {'b':question, 'ua':u_answer, 'a':answer})
#     else:
#         return render(request, 'answer.html')

def update_test(request):
    return render(request, 'update.html')

def question(request):
    form = Answer(request.POST)
    answer = ''
    question = ''
    u_answer = ''

    # if request.session.has_key('u_answer'):
    #     question = request.session['question']
    #     answer = request.session['answer']
    #     u_answer = request.session['u_answer']
    #     c = ''
    #     return render(request, 'question.html', {'b':question, 'ua':u_answer, 'a':answer, 'c':c})
    # else:

    #     equ = Equation(1, random.randint(1, 2), 1, random.randint(1, 2))
    #     equ.answer()
    #     question = equ.question
    #     answer = equ.answer
    #     request.session['question'] = question
    #     request.session['answer'] = answer
    if request.session.has_key('u_answer'):
        if request.session.has_key('points'):
            points = request.session['points']
        else:
            points = 0
            if u_answer2 == answer_2:
                points += 1
        request.session['points'] = points
        c = ''

        return render(request, 'answer.html', {'b':question, 'ua':u_answer, 'a':answer, 'c':c, 'a2':answer_2, 'ua2':u_answer2, 'points':points})
    else:
    
    
    
        if form.is_valid():
            u_answer = form.cleaned_data.get('aswer')
            request.session['u_answer'] = u_answer
            
            # if 'problem' in request.POST:
            #     print("Work 1")
            #     request.session['u_answer'] = 'txt'
            #     print("Has worked 2")
            # else:
                # print("No work 3")

            ################################################
            # And make sure to remove this sesction as well
            # if request.session.has_key('poop'):
            #     request.session['u_answer'] = 'close'
            #     print("\nworked\n")
            # else:
            #     print("\nno work\n")
            #     request.session['poop'] = 'hey'
            #################################################


            # if request.session.has_key('u_answer'):
            #     pass
            # else:
            #     request.session['u_answer'] = 'poop'

        equ = Equation(1, random.randint(-4, 4), 1, random.randint(-4, 4))
        equ.answer()
        question = equ.question
        answer = equ.answer
        request.session['question'] = question
        request.session['answer'] = answer

        if request.session.has_key('u_answer'):
            question = request.session['question']
            answer = str(request.session['answer'])
            u_answer = str(request.session['u_answer'])
            u_answer2 = str(fixe(u_answer))
            answer_2 = str(fixe(answer))
            c=''
            points = request.session['points']
            return render(request, 'answer.html', {'b':question, 'ua':u_answer, 'a':answer, 'c':c, 'a2':answer_2, 'ua2':u_answer2, 'points':points})

        else:
            return render(request, 'question.html', {'Answer':answer, 'Question':question, 'form':form})
