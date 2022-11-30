from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.template import loader

from .models import Question

"""
def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template('polls/index.html')
    context = {
        'latest_question_list': latest_question_list,
    }
    return HttpResponse(template.render(context, request))
"""

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)
def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)

import matplotlib.pyplot as plt
from io import StringIO
import numpy as np

def return_graph():

    x = np.arange(0,np.pi*3,.1)
    y = np.sin(x)

    fig = plt.figure()
    plt.plot(x,y)

    imgdata = StringIO()
    fig.savefig(imgdata, format='svg')
    imgdata.seek(0)

    data = imgdata.getvalue()
    return data

def home(request):
    context['graph'] = return_graph()
    return render(request, 'x/dashboard.html', context)