from django.http import HttpResponse
from django.shortcuts import render
from .models import *


def index(request):  # HttpRequest
    return render(request, 'index.html')


def result(request):
    return HttpResponse("Hash result page")


