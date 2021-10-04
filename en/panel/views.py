from django.shortcuts import render, get_object_or_404
from django.http import Http404

from .models import Question, HomeSlider


# Create your views here.

def home(request):
    slider_list = HomeSlider.objects.order_by('-pub_date')[:5]
    print(len(slider_list))
    context = {
        'slider_list': slider_list,
    }
    return render(request, 'panel/index.html', context)


def panel(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {
        'latest_question_list': latest_question_list,
    }
    return render(request, 'panel/index.html', context)


def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'panel/detail.html', {'question': question})


def results(request, question_id):
    response = "You're looking at the results of question %s."
