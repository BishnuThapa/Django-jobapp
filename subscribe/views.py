from django.shortcuts import render
from .models import Subscribe
# Create your views here.


def subscribe(request):
    email_error_empty = ""
    # Server side validation in the views
    # if request.method == "POST":
    if request.POST:
        firs_tname = request.POST['firstname']
        last_name = request.POST['lastname']
        email = request.POST['email']
        if email == "":
            email_error_empty = "No Email Entered."
        subscribe = Subscribe(
            first_name=firs_tname, last_name=last_name, email=email)
        subscribe.save()
    context = {
        'email_error_empty': email_error_empty,
    }
    return render(request, 'subscribe/subscribe.html', context)
