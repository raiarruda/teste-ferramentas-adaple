from django.conf import settings
from django.conf.urls import url
from django.contrib import admin
from django.contrib.staticfiles.urls import static, staticfiles_urlpatterns
from mysite.audio.views import *
from django.urls import path, include
#appname= "audio"
urlpatterns = [
 #   url(r'^admin/', admin.site.urls),
    path('', model_form_upload, name='views.model_form_upload'),
    path('list', list_files, name='views.list_files'),
]


if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT)
    urlpatterns += staticfiles_urlpatterns()
