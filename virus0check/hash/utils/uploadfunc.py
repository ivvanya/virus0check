from django.shortcuts import render
from hashlib import md5
from datetime import datetime
from .FileInfo.ExeInfo import get_exe_info
from ..forms import FileUploadForm
from ..models import MalwareHash


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
            if MalwareHash.objects.filter(hash=md5_hash).exists():
                return render(request, 'virus0check/result.html', {'result': 'Файл заражен! :(',
                                                                   'file_info': f'{get_exe_info(file_path)}'})
            else:
                return render(request, 'virus0check/result.html', {'result': 'Файл безопасен :)',
                                                                   'file_info': f'{get_exe_info(file_path)}'})
    else:
        form = FileUploadForm()
    return render(request, 'virus0check/upload.html', {'form': form})
