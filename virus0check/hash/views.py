from .utils.uploadfunc import file_upload_func


def file_upload_view(request):
    return file_upload_func(request)
