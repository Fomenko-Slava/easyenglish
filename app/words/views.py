from django.shortcuts import render
from django.http import HttpResponse
import sys

def index(request):
    print(sys.path)
    print(1)
    print(request)
    print(2)
    return HttpResponse("Hello, world. You're at the polls index." + '<br/>'.join(sys.path))
