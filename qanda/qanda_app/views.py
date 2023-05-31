from django.shortcuts import render
from django.views import View
from django.views.generic import ListView
from django.http import Http404
from django.http import HttpResponse
from .models import Question


class QuestionsView(ListView):
    template_name = "index.html"
    context_object_name = 'questions'
    def get_queryset(self, *args, **kwargs):
        latest_question_list = Question.objects.order_by('-pub_date')[:5]
        return latest_question_list

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    output = ', '.join([q.content for q in latest_question_list])
    return render(latest_question_list,'index.html')

def question_detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'detail.html', {'question': question})