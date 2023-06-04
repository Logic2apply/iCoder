from django.urls import path
from authentication import views

urlpatterns = [
    path("signup/", views.handleSignUp, name="SignUp"),
    path("signin/", views.handleSignIn, name="SignIn"),
    path("signout/", views.handleSignOut, name="SignOut")
]
