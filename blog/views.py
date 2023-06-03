from django.contrib import messages
from django.shortcuts import redirect, render

from blog.models import BlogPost

# Create your views here.
def blogHome(request):
    posts = BlogPost.objects.all()
    context = {
        "posts": posts
    }
    return render(request, "blog/blogHome.html", context=context)


def blogPost(request, sno, slug):
    try:
        Post = BlogPost.objects.get(sno=sno, slug=slug)
        context = {
            "post":Post
        }
        return render(request, "blog/blogPost.html", context)
    
    except Exception as e:    
        messages.error(request, f"No such blog post found. Please check the url. {e}")
        return redirect("BlogHome")