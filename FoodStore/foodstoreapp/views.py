from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
# Create your views here.


def home(request):
    return redirect(foodstore_home)


"""
In order to get home page, we need to be
logged in. In case user is not logged in
he is redirected to sign-in/
"""
@login_required(login_url='/foodstore/sign-in/')
def foodstore_home(request):
    return render(request, 'foodstore/home.html')
