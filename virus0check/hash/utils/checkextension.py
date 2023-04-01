import os
from ..forms import FileUploadForm
from django.shortcuts import render
from .FileInfo.ExeInfo import file_exe_info
from .FileInfo.ImgInfo import file_img_info
from .FileInfo.MpxInfo import file_mpx_info
from .FileInfo.PdfInfo import file_pdf_info
from .FileInfo.OfficeInfo import file_office_info

exe_array = {
    '.EXE',
    '.exe'
}

img_array = {
    '.JPG',
    '.PNG',
    '.jpg',
    '.png'
}

mpx_array = {
    '.mp3',
    '.MP3',
    '.mp4',
    '.MP4'
}

office_array = {
    '.docx',
    '.DOCX',
    '.DOC',
    '.doc',
    '.pptx',
    '.PPTX',
    '.xlsx',
    '.XLSX'
}

pdf_array = {
    '.PDF',
    '.pdf'
}


def check_extension(file_path, status, request):
    path, name = os.path.splitext(file_path)
    if status:
        statusname = 'Файл заражен'
    else:
        statusname = 'Файл безопасен'
    if any(item in name for item in exe_array):
        return render(request, 'virus0check/result.html', {'result': f'{statusname}',
                                                           'file_info': f'{file_exe_info(file_path)}'})
    elif any(item in name for item in img_array):
        return render(request, 'virus0check/result.html', {'result': f'{statusname}',
                                                           'file_info': f'{file_img_info(file_path)}'})
    elif any(item in name for item in mpx_array):
        return render(request, 'virus0check/result.html', {'result': f'{statusname}',
                                                           'file_info': f'{file_mpx_info(file_path)}'})
    elif any(item in name for item in office_array):
        return render(request, 'virus0check/result.html', {'result': f'{statusname}',
                                                           'file_info': f'{file_office_info(file_path)}'})
    elif any(item in name for item in pdf_array):
        return render(request, 'virus0check/result.html', {'result': f'{statusname}',
                                                           'file_info': f'{file_pdf_info(file_path)}'})
    else:
        return render(request, 'virus0check/result.html', {'result': f'{statusname}',
                                                           'file_info': 'Нет метаданных для этого расширения файла'})

    form = FileUploadForm()
    return render(request, 'virus0check/upload.html', {'form': form})

