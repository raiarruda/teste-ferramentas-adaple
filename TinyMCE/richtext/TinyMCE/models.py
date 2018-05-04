from django.db import models
from tinymce import HTMLField

class MyModel(models.Model):

    content = HTMLField('Content')