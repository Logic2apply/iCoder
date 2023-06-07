from django.contrib import messages
from django.shortcuts import redirect, render

from blog.models import BlogPost, BlogComment

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
        comments = BlogComment.objects.filter(post = Post)
        context = {
            "post":Post,
            "comments":comments
        }
        return render(request, "blog/blogPost.html", context)
    
    except Exception as e:    
        messages.error(request, f"No such blog post found. Please check the url. {e}")
        return redirect("BlogHome")
    

def postComment(request):
    if request.method == "POST":
        comment = request.POST.get("comment")
        user = request.user
        postsno = request.POST.get("postsno")
        post = BlogPost.objects.get(sno = postsno)

        comment = BlogComment(comment = comment, user = user, post = post)
        comment.save()

        messages.success(request, "Your comment has been posted.")
        return redirect(f"/blog/{post.sno}/{post.slug}/")
    return 