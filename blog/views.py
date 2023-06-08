from django.contrib import messages
from django.shortcuts import redirect, render
from blog.templatetags import extras
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
        Post.views += 1
        Post.save()
        
        comments = BlogComment.objects.filter(post = Post, parent=None)
        replies = BlogComment.objects.filter(post=Post).exclude(parent=None)
        repDict = {}
        for reply in replies:
            if reply.parent.sno not in repDict.keys():
                repDict[reply.parent.sno] = [reply]
            else:
                repDict[reply.parent.sno].append(reply)
        context = {
            "post":Post,
            "comments":comments,
            "repDict":repDict
        }
        return render(request, "blog/blogPost.html", context)
    
    except Exception as e:    
        messages.error(request, f"No such blog post found. Please check the url. {e}")
        return redirect("BlogHome")
    

def postComment(request):
    if request.method == "POST":
        comment = request.POST.get("comment")
        user = request.user

        # Get post 
        postsno = request.POST.get("postsno")
        post = BlogPost.objects.get(sno = postsno)

        # Get parent comment and check for it
        parentsno = request.POST.get("parentsno")
        if parentsno == "":
            comment = BlogComment(comment = comment, user = user, post = post)
            comment.save()
            messages.success(request, "Your comment has been posted successfully.")
        else:
            parent = BlogComment.objects.get(sno = parentsno)
            comment = BlogComment(comment = comment, user = user, post = post, parent = parent)
            comment.save()
            messages.success(request, "Your reply has been posted successfully.")

        return redirect(f"/blog/{post.sno}/{post.slug}/")
    
    else:
        messages.error(request, "Unable to post comment!")
        return redirect("Home")