from django.shortcuts import render
from hashlib import md5
from datetime import datetime
from ..forms import FileUploadForm
from ..models import MalwareHash
from .checkextension import check_extension


def file_upload_func(request):
    if request.method == 'POST':
        form = FileUploadForm(request.POST, request.FILES)
        if form.is_valid():
            file = request.FILES['file']
            content = file.read()

            file_path = f'hash/checked/{datetime.now().strftime("%m-%d-%Y_%H-%M-%S")}_{file._name}'
            with open(file_path, 'wb') as file:
                file.write(content)

            md5_hash = md5(content).hexdigest()
            status = MalwareHash.objects.filter(hash=md5_hash).exists()
            return check_extension(file_path, status, request)
    else:
        form = FileUploadForm()
    return render(request, 'virus0check/upload.html', {'form': form})
