from django.contrib import admin
from blog.models import BlogPost, BlogPostAdmin, BlogComment, BlogCommentAdmin

# Register your models here.
admin.site.register(
    BlogPost,
    BlogPostAdmin
)
admin.site.register(
    BlogComment,
    BlogCommentAdmin
)