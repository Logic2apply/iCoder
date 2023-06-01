from django.utils import timezone
from django.db import models
from django.contrib import admin

# Create your models here.
class Contact(models.Model):
    sno = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, default="")
    phone = models.CharField(max_length=14, default="")
    email = models.CharField(max_length=100, default="")
    message = models.CharField(max_length=5000, default="")
    dateAdded = models.DateField(auto_now_add=True)

    def __str__(self) -> str:
        return f"{self.sno} - {self.name} - {self.email} - {self.phone} - {self.message[:100]}..."


class ContactAdmin(admin.ModelAdmin):
    list_display = [
        "sno",
        "name",
        "email",
        "phone",
        "message",
        "dateAdded"
    ]