from django.shortcuts import render
from .models import Subscribe
from subscribe.forms import SubscribeForm
# Create your views here.


def subscribe(request):
    subscribe_form = SubscribeForm()
    email_error_empty = ""
    if request.POST:
        subscribe_form = SubscribeForm(request.POST)
        if subscribe_form.is_valid():
            print("Valid Form")
    # Server side validation in the views
    # if request.method == "POST":
    # if request.POST:
        # firs_tname = request.POST['firstname']
        # last_name = request.POST['lastname']
        # email = request.POST['email']
        # if email == "":
        #     email_error_empty = "No Email Entered."
        # subscribe = Subscribe(
        #     first_name=firs_tname, last_name=last_name, email=email)
        # subscribe.save()
    context = {
        'form': subscribe_form,

        # 'email_error_empty': email_error_empty,
    }
    return render(request, 'subscribe/subscribe.html', context)
