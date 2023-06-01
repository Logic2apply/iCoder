from django.contrib import admin
from home.models import Contact, ContactAdmin

# Register your models here.
admin.site.register(
    Contact,
    ContactAdmin
)