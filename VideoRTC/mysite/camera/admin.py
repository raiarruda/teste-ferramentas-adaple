from django.contrib import admin
from .models import db_video, MyModel

# Register your models here.

admin.site.register(db_video)
admin.site.register(MyModel)