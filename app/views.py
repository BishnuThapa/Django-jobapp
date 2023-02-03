from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def home(request):
    return HttpResponse("Hello from Homepage")


def job_detail(request, id):
    return HttpResponse(id)
