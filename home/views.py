# from django.http import HttpResponse
import time
from django.shortcuts import render
from home.models import Contact
from django.contrib import messages
from blog.models import BlogPost

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


def search(request):
    if request.method == 'GET':
        initial = time.perf_counter()

        query = request.GET.get('search')
        if len(query) > 80 or len(query) < 3:
            posts = []
        else:
            postsTitle = BlogPost.objects.filter(title__icontains=query)
            postsContent = BlogPost.objects.filter(content__icontains=query)
            posts = postsTitle.union(postsContent)

        final = time.perf_counter()
        timeTaken = final - initial
        context = {
            'time':timeTaken,
            'query':query,
            'posts':posts
        }

        if posts.count() == 0:
            messages.error(request, "No search results found. Please check your query!")
        return render(request, "home/search.html", context=context)