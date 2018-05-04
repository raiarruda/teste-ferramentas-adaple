from django.db import models
import os                                               
from  django.core.files.storage import FileSystemStorage
from ckeditor.fields import RichTextField

STATIC_CUR_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'static')

upload_storage = FileSystemStorage(location=STATIC_CUR_DIR)

# Create your models here.

class db_video(models.Model):
    nome = models.CharField(max_length=20)
    video = models.FileField(upload_to='media/videosenviados', storage=upload_storage, default="media/none.mp4")


class MyModel(models.Model):

    content = RichTextField()
