import re
from django.http import HttpResponse
from django.shortcuts import redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout


# Create your views here.
def handleSignUp(request):
    if request.method == "POST":
        username = request.POST.get("username")
        fname = request.POST.get("fname")
        lname = request.POST.get("lname")
        email = request.POST.get("email")
        password1 = request.POST.get("password1")
        password2 = request.POST.get("password2")

        # Check for valid entries
        if username == "" or fname == "" or lname == "" or email == "" or password1 == "" or password2 == "":
            messages.error(request, "You can't left fields blank. Please check them again!")

        if len(username) > 15:
            messages.error(request, "Username can't be greater than 15 characters!")
            
        if not username.isalnum():
            messages.error(request, "Username should contain only letters and numbers!")

        if password1 != password2:
            messages.error(request, "Please check your entered passwords!")
            
        else:
            user = User.objects.create_user(
                username = username,
                email = email,
                password = password1,
                first_name = fname,
                last_name = lname
            )
            user.save()
            messages.success(request, "Your iCoder Account has been created!")
        return redirect("Home")
    else:
        messages.error(request, "Error 404! Page Not Found!")
        return redirect("Home")

def handleSignIn(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(username = username, password = password)
        if user is not None:
            login(request, user)
            messages.success(request, "Login successful")
            return redirect("Home")

        else:
            messages.error(request, "No user found! Please check your credentials!")
            return redirect("Home")

    else:
        messages.error(request, "Error 404! Page Not Found!")
        return redirect("Home")

def handleSignOut(request):
    if request.user.is_authenticated:
        logout(request)
        messages.success(request, "User successfully signed out!")
        return redirect("Home")
    else:
        return redirect("Home")

