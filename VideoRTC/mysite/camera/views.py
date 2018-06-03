import uuid
from django.http import (HttpResponse, HttpResponseRedirect, StreamingHttpResponse)
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from .forms import MyForm, UploadFileForm
#from apiclient.discovery import build
from .models import MyModel, db_video
from django.conf import settings
from django.core.files.storage import FileSystemStorage


def visualizarVideos(request):
    videos = db_video.objects.all()
    template = 'camera/testevisualizarvideo.html'

    return render (request, template, {'videos': videos})

@csrf_exempt
def video(request):
    
    if request.method == 'POST' and request.FILES['video_file']:
        myfile = request.FILES['video_file']
        form = UploadFileForm(request.POST, request.FILES)
        fs = FileSystemStorage()
        filename = fs.save('video/'+ myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        print(uploaded_file_url)
        video = db_video.objects.create(nome=myfile.name, video=uploaded_file_url)
        print (video.video)
        return render(request, 'camera/video.html', {
            'uploaded_file_url': uploaded_file_url
        })
    return render(request, 'camera/video.html')

''' def video(request):
    if request.method == "POST":
        #video = 
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            
            file_name = handle_uploaded_file(request.FILES['video_file'])
      #      video = form.save(commit=False)
       #     video.video=file_name
        #    video.save()
            return HttpResponse("video gravado", content_type='plain/text')
       #     return HttpResponseRedirect('/success/url/')
        else:
            # content_type="application/json"
            return HttpResponse('NÃO GRAVOU', content_type='plain/text')
    else:
        return render(request, 'camera/video.html')


def handle_uploaded_file(f):
    file_name = uuid.uuid4().hex+'.webm'
    with open('media/video'+file_name, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)
    return file_name
 '''
 

def formulario(request):
    template ='camera/teste.html'

    
    if request.method == "POST":
            form = MyForm(request.POST)
            if form.is_valid():

                f = form.save(commit=False)
                f.save()
                

                return HttpResponse("form salvo", content_type='plain/text')
            else:
                return ( request, template, {'form':form})

    else:
        form = MyForm()
        return render( request, template, {'form':form})

    return render( request, template, {'form':form})

def ver(request):

    template='camera/ver.html'
    modelos = MyModel.objects.all()

    return render(request,template,{'modelos':modelos})
