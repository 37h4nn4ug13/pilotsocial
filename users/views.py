from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login

# Create your views here.
def user_login(request): 
    if (request.method == 'POST'):  
        user = authenticate(username=request.POST['username'], password=request.POST['password'])
        if user is not None:
            login(request, user)
            return redirect("home")
    context = {

    }
    return render(request, "login.html", context)


def index(request) :
    return HttpResponse("Home")
