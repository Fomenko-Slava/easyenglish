from django.db.models import Q
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.mixins import RetrieveModelMixin, ListModelMixin, UpdateModelMixin, DestroyModelMixin, \
    CreateModelMixin
from rest_framework.viewsets import GenericViewSet

from core.utils_helper import prn, analyze
#from django.db import connection
from words.serializers import WordSerializer

from .models import *


# пример с OR
# user_lists = WordList.objects.filter(Q(user=None) | Q(user_id=request.user.id))
# def newfunc(n):
#     def myfunc(x):
#         prn(x)
#         return x + n
#     return myfunc


@analyze
def index(request):
    """Главная страница выводятся все общие списки и списки пользователя"""

    context = {'general_lists': WordList.objects.filter(user=None)}

    if request.user.is_authenticated:
        context['user_lists'] = WordList.objects.filter(user_id=request.user.id)

    context['test'] = 'шЛа Саша по Шосе и соСалА СушкУ'

    context['borsh_lists'] = WordList.objects.filter(user__username='slav')

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


class WordView(RetrieveModelMixin,
                  UpdateModelMixin,
                  DestroyModelMixin,
                  ListModelMixin,
                  CreateModelMixin,
                  GenericViewSet):
    serializer_class = WordSerializer
    #permission_classes = (IsAuthenticated, ModelPermissions)
    queryset = Word.objects.all()
    filter_backends = (DjangoFilterBackend, SearchFilter, OrderingFilter)
    filter_fields = ('word_ru', 'word_en')
    search_fields = ('word_ru', 'word_en')
    ordering_fields = ('id', 'word_ru', 'word_en')
    ordering = ('word_ru',)

#class WordViewSet(viewsets.ModelViewSet):
#    """
#    #    API endpoint that allows words to be viewed or edited.
#    #    """
#    queryset = Word.objects.all()
#    serializer_class = WordSerializer

#class UserViewSet(viewsets.ModelViewSet):
#    """
#    API endpoint that allows users to be viewed or edited.
#    """
#    queryset = User.objects.all().order_by('-date_joined')
#    serializer_class = UserSerializer
#
#
#class GroupViewSet(viewsets.ModelViewSet):
#    """
#    API endpoint that allows groups to be viewed or edited.
#    """
#    queryset = Group.objects.all()
#    serializer_class = GroupSerializer
