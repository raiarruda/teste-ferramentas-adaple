"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from mysite.camera import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings
from mysite.audio import urls as audio_urls
urlpatterns = [
    path('audio/', include(audio_urls)),
    path('admin/', admin.site.urls),
    path('video/', views.video, name='camera'),
   # path('video/', views.VideoView, name='camera'),
    
    path('visualizar/', views.visualizarVideos, name='visualizarVideos'),
    #TODO: 
    
    path('form/', views.formulario, name='home'),
    path('ver/', views.ver, name='ver'),

]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT)
    urlpatterns += staticfiles_urlpatterns()
