from django.contrib import admin

# Register your models here.
from richtext.TinyMCE.models import MyModel

admin.site.register(MyModel)
