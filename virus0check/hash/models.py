from django.db import models


class MalwareHash(models.Model):
    hash = models.CharField(max_length=128)

    
def __str__(self):
    return self.title
