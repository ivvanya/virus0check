from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def index(request):  # HttpRequest
    return HttpResponse("Hash application page")


def result(request):
    return HttpResponse("Hash result page")
