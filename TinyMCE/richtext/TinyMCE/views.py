from django.shortcuts import render,redirect
from richtext.TinyMCE.forms import MyForm
from richtext.TinyMCE.models import MyModel
from django.contrib import messages
# Create your views here.
def home(request):
    template ='teste.html'

    
    if request.method == "POST":
            form = MyForm(request.POST)
            if form.is_valid():

                f = form.save(commit=False)
                f.save()
                messages.success(request, 'EDP respondida com sucesso')

                return redirect('home')
            else:
                messages.info(request, 'não respondida')

    else:
        form = MyForm()
        return render( request, template, {'form':form})

    return render( request, template, {'form':form})

def ver(request):

    template='ver.html'
    modelos = MyModel.objects.all()

    return render(request,template,{'modelos':modelos})