from django.db import models
from django.contrib import admin
from django.contrib.auth.models import User
from django.utils.text import slugify
from tinymce.widgets import TinyMCE


# Create your models here.
class BlogPost(models.Model):
    sno = models.AutoField(primary_key=True)
    title = models.CharField(max_length=500, default="")
    content = models.TextField(max_length=50000, default="")
    author = models.CharField(max_length=50, default="")
    slug = models.CharField(max_length=150, default="", unique=True)
    views = models.IntegerField(default=0)
    dateAdded = models.DateTimeField(auto_now_add=True)

    def save(
        self, force_insert=False, force_update=False, using=None, update_fields=None
    ):
        self.slug = slugify(self.title)
        if update_fields is not None and "title" in update_fields:
            update_fields = {"slug"}.union(update_fields)
        super().save(
            force_insert=force_insert,
            force_update=force_update,
            using=using,
            update_fields=update_fields,
        )

    def __str__(self) -> str:
        return f"{self.sno} - {self.title}"


class BlogPostAdmin(admin.ModelAdmin):
    list_display = [
        "sno",
        "title",
        "content",
        "author",
        "slug",
        "dateAdded"
    ]
    formfield_overrides = {
        models.TextField: {'widget': TinyMCE()}
    }


# Comments
class BlogComment(models.Model):
    sno = models.AutoField(primary_key = True)
    comment = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(BlogPost, on_delete=models.CASCADE)
    parent = models.ForeignKey("self", on_delete=models.CASCADE, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"{self.user} posted {self.comment} on post {self.post}. Its parent is {self.parent}"

class BlogCommentAdmin(admin.ModelAdmin):
    list_display = [
        "sno",
        "comment",
        "user",
        "post",
        "parent",
        "timestamp"
    ]
