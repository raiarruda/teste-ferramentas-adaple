from django.shortcuts import render
from django.http import HttpResponse, StreamingHttpResponse, HttpResponseRedirect
from .models import db_video
from .forms import UploadFileForm
import uuid  # TODO
from apiclient.discovery import build
from .models  import db_video

def visualizarVideos(request):
    videos = db_video.objects.all()
    template = 'camera/testevisualizarvideo.html'

    return render (request, template, {'videos': videos})

def video(request):

    
    if request.method == "POST":
        #video = 
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            
            file_name = handle_uploaded_file(request.FILES['video_file'])
            video = form.save(commit=False)
            video.video=file_name
            video.save()
            return HttpResponse("video gravado", content_type='plain/text')
       #     return HttpResponseRedirect('/success/url/')
        else:
            # content_type="application/json"
            return HttpResponse('teste2', content_type='plain/text')
    else:
        return render(request, 'camera/video.html')


def handle_uploaded_file(f):
    file_name = uuid.uuid4().hex+'.webm'
    with open('media/video'+file_name, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)
    return file_name


def audio(request):
    if request.method == "POST":
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            file_name = handle_uploaded_file2(request.FILES['audio_file'])
            return HttpResponse("audio gravado", content_type='plain/text')
       #     return HttpResponseRedirect('/success/url/')
        else:
            # content_type="application/json"
            return HttpResponse('teste - audio', content_type='plain/text')
    else:   
        return render(request, 'camera/audio.html')


def video2(request):

    return render(request, 'camera/video2.html')


def handle_uploaded_file2(f):
    file_name = uuid.uuid4().hex+'.mp3'
    with open('media/audio'+file_name, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)
    return file_name
    
    
        
