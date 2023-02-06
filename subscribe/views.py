from django.shortcuts import render

# Create your views here.


def subscribe(request):
    email_error_empty = ""
    # Server side validation in the views
    if request.method == "POST":
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        email = request.POST['email']
        if email == "":
            email_error_empty = "No Email Entered."
        subscribe_user = subscribe(
            firstname=firstname, lastname=lastname, email=email)
        subscribe_user.save()
    context = {
        'email_error_empty': email_error_empty,
    }
    return render(request, 'subscribe/subscribe.html', context)
