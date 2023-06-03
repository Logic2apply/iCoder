from django.db import models
from django.contrib import admin
from django.utils.text import slugify

# Create your models here.
class BlogPost(models.Model):
    sno = models.AutoField(primary_key=True)
    title = models.CharField(max_length=500, default="")
    content = models.TextField(max_length=50000, default="")
    author = models.CharField(max_length=50, default="")
    slug = models.TextField(max_length=150, default="", unique=True)
    dateAdded = models.DateField(auto_now_add=True)

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