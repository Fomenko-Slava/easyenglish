# -*- coding: utf-8 -*-
from django.contrib.auth.models import User
from django.core.management.base import BaseCommand
from core.time_helper import timeit
from core.utils_helper import prn, analyze
from words.models import WordList, WordListVal


#@analyze
@timeit
def test_script():
    pass

    #wordlist = WordList()
    #wordlist.title = 'первый список'
    #wordlist.user = User.objects.first()
    #wordlist.save()

    #prn(WordList.objects.all())

    prn(WordListVal.objects.all())




class Command(BaseCommand):

    def handle(self, *args, **options):
        print('Test script started')
        test_script()
        print('Test script finished')