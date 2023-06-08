# from django.http import HttpResponse
import time
from django.http import JsonResponse
from django.shortcuts import redirect, render
from home.models import Contact
from django.contrib import messages
from blog.models import BlogPost

# Create your views here.
def home(request):
    posts = BlogPost.objects.all().order_by("-views")[:5]
    context = {
        "posts":posts
    }
    return render(request, "home/home.html", context=context)


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
    

def duplicator(request):
    return redirect("Home")
    # sno = int(request.GET.get("sno"))
    # multiplier = int(request.GET.get("multiplier"))
    # # sno = 2
    # # multiplier = 10

    # try:
    #     post = BlogPost.objects.get(sno = sno)
    #     for i in range(multiplier):
    #         title = f"{post.title} copy {i}"
    #         slug = f"{post.slug}-copy-{i}"
    #         newPost = BlogPost(title = title, content=post.content, author=post.author, slug=slug, views=post.views)
    #         newPost.save()
    #         message = f"Successfully made {multiplier} from post sno:{sno}"
    #         messages.success(request, message)
    # except Exception as e:
    #     message = f"An error occured as: {e}"
    #     messages.error(request, message)
    
    # return JsonResponse({"message":message})