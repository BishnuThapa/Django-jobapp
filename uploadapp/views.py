from django.shortcuts import render
from uploadapp.forms import UploadForm
# Create your views here.


def upload_image(request):
    form = UploadForm()
    context = {
        'form': form
    }
    return render(request, 'uploadapp/add_image.html', context)
