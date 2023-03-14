import hashlib
from django.http import HttpResponseRedirect


def handle_uploaded_file(file):
    with open('Git-2.39.2-64-bit.exe', 'rb') as f:
        hsh = hashlib.md5()
        while True:
            data = f.read(2048)
            if not data:
                break
            hsh.update(data)
        rez = hsh.hexdigest()

        # print(rez)

        f.read()

def upload_file(request):
    # Если метод POST
    if request.method == 'POST':
        # Заполняем форму полученными данными
        form = UploadFileForm(request.POST, request.FILES)
        # Если данные валидны
        if form.is_valid():
            # обрабатываем файл
            handle_uploaded_file(request.FILES['file'])
            # перенаправляем на другую страницу
            return HttpResponseRedirect('/success/url/')
    # Если другой метод (обычно GET)
    else:
        form = UploadFileForm()
    # Выводим форму загрузки
    return render_to_response('upload.html', {'form': form})