from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="Home"),
    path("contact/", views.contact, name="Contact"),
    path("about/", views.about, name="About"),
    path("search/", views.search, name="Search"),
    path("duplicatequery/", views.duplicator, name="duplicator")
]