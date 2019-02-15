# -*- coding: utf-8 -*-
from django.contrib.auth.models import User
from django.core.management.base import BaseCommand
from core.time_helper import timeit
from core.utils_helper import prn, analyze
from words.models import WordList, WordListVal


@analyze
@timeit
def test_script():
    #pass

    #wordlist = WordList()
    #wordlist.title = 'первый список'
    #wordlist.user = User.objects.first()
    #wordlist.save()

    #prn(WordList.objects.all())


    #Blog.objects.filter(entry__headline__contains='Lennon',
    #                    entry__pub_date__year=2008)

    #first_user = User.objects.first()
    #prn(first_user)
#
    users = User.objects.filter(author_word_list__created_at__year=2018)\
        .filter(author_word_list__title__contains='первый')
#
    prn(users)


class Command(BaseCommand):

    def handle(self, *args, **options):
        print('Test script started')
        test_script()
        print('Test script finished')