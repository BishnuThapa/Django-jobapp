from django.shortcuts import render
from uploadapp.forms import UploadForm


def upload_image(request):
    if request.method == 'POST':
        form = UploadForm(request.POST, request.FILES)
        if form.is_valid:
            form.save()
    else:
        form = UploadForm()
    context = {'form': form}
    return render(request, 'uploadapp/add_image.html', context)
