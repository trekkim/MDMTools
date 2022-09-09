from django.db import models
from django.contrib.auth.models import User

class MyModel(models.Model):
    class Meta:
        permissions = (
            ('can_delete_device_id', 'User can delete Device ID.'),
        )

    
class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    pdf = models.FileField(upload_to='books/pdfs/')

    def __str__(self):
        return self.title