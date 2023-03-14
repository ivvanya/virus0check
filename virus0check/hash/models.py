from django.db import models


class MD5hashes(models.Model):
    hash = models.CharField(max_length=32)


class UploadFiles(models.Model):
    file = models.FileField(upload_to="files")


def __str__(self):
    return self.title
