import os
from django.core.files.base import File
from django.shortcuts import render, redirect
from mysite.audio.forms import AudioflForm
from mysite.audio.models import Audiofl


def model_form_upload(request):
    if request.method == 'POST':
        form = AudioflForm(request.POST, request.FILES)
        if form.is_valid():
            newform = form.save(commit=False)
            djfile = File(request.FILES['data_blob'])
            newform.fl.save(request.FILES['data_blob'].name, djfile)
            newform.save()

            # convert to fix the duration of audio
            file_path = newform.fl.path
            os.system(
                "/usr/bin/mv %s %s" % (
                    file_path, (file_path + '.original'))
            )
            os.system(
                "/usr/bin/ffmpeg -i %s -c copy -fflags +genpts %s" % (
                    (file_path + '.original'), file_path)
            )

            return redirect('/')
    else:
        form = AudioflForm()
    return render(request, 'audio/model_form_upload.html', {
        'form': form
    })


def list_files(request):
    files = Audiofl.objects.all().order_by('uploaded_at')

    return render(request, 'audio/list_files.html', {
        'files': files
    })
