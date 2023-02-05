from django.shortcuts import render
from django.http import HttpResponse
from .models import JobPost
# Create your views here.


def home(request):
    jobs = JobPost.objects.all()
    # jobs=JobPost.objects.order_by("?") --> get values in random order
    context = {
        'jobs': jobs
    }
    # return HttpResponse("Hello from Homepage")
    return render(request, 'app/index.html', context)


def job_detail(request, id):
    # return HttpResponse(id)
    job = JobPost.objects.get(id=id)
    context = {
        'job': job
    }
    return render(request, 'app/job_detail.html', context)
