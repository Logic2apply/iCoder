# from django.http import HttpResponse
from django.shortcuts import render
from home.models import Contact
from django.contrib import messages

# Create your views here.
def home(request):
    return render(request, "home/home.html")


def contact(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        message = request.POST.get("message")

        try:
            contact = Contact(name=name, email=email, phone=phone, message=message)
            contact.save()
        
            # Return a success message
            messages.success(request, "Message sent successfully")

        except Exception as e:
            messages.error(request, "Something went wrong!")
        return render(request, "home/contact.html")

    return render(request, "home/contact.html")


def about(request):
    return render(request, "home/about.html")