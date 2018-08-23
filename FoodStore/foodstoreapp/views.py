from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from foodstoreapp.forms import UserForm, FoodStoreForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
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
    return render(request, 'foodstore/home.html', {})


def foodstore_sign_up(request):
    user_form = UserForm()              # get data from User html forms
    foodstore_form = FoodStoreForm()    # get data from FoodStore html forms

    if request.method == "POST":        # esli huyachim POST "submit" to go her
        user_form = UserForm(request.POST)
        foodstore_form = FoodStoreForm(request.POST, request.FILES) # we can get files too from this form

        if user_form.is_valid() and foodstore_form.is_valid():      # check if data is valid
            new_user = User.objects.create_user(**user_form.cleaned_data)
            new_foodstore = foodstore_form.save(commit=False)       # create just object in RAM "commit=False"
            new_foodstore.user = new_user                           # assign new user
            new_foodstore.save()                                    # save to DataBase

            login(request, authenticate(                            # try to login just after sign_up
                username = user_form.cleaned_data["username"],
                password = user_form.cleaned_data["password"]
            ))

            return redirect(foodstore_home)

    return render(request, 'foodstore/sign_up.html', {
        "user_form": user_form,
        "foodstore_form": foodstore_form
    })
