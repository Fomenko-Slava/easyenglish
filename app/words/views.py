from django.db.models import Q
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from core.utils_helper import prn, analyze
#from django.db import connection

from .models import *

# пример с OR
#user_lists = WordList.objects.filter(Q(user=None) | Q(user_id=request.user.id))

@analyze
def index(request):
    """Главная страница выводятся все общие списки и списки пользователя"""

    context = {'general_lists': WordList.objects.filter(user=None)}

    if request.user.is_authenticated:
        context['user_lists'] = WordList.objects.filter(user_id=request.user.id)

    context['test'] = 'шЛа Саша по Шосе и соСалА СушкУ'

    return render(request, 'words/wordlists_list.html', context)


def word_list(request, id):
    """Страница одного списка"""

    context = {'word_list': get_object_or_404(WordList, pk=id)}

    return render(request, 'words/word_list.html', context)


def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)


def add_word_to_list(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
