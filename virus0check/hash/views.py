from django.http import HttpResponse
from django.shortcuts import render
from .models import *
from django.urls import reverse
from hashlib import md5
from .forms import FileUploadForm
from .models import MalwareHash


def file_upload_view(request):
    if request.method == 'POST':
        form = FileUploadForm(request.POST, request.FILES)
        if form.is_valid():
            file = request.FILES['file']
            content=file.read()
            md5_hash=md5(content).hexdigest()
            if MalwareHash.objects.filter(hash=md5_hash).exists():
                return render(request, 'virus0check/result.html', {'result': 'Файл заражен! :('})
            else:
                return render(request, 'virus0check/result.html', {'result': 'Файл безопасен :)'})
    else:
        form=FileUploadForm()
    return render(request, 'virus0check/upload.html', {'form': form})


def index(request):  # HttpRequest
    return render(request, 'index.html')


def result(request):
    return HttpResponse("Hash result page")