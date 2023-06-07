from django.urls import path
from . import views

urlpatterns = [
    path("", views.blogHome, name="BlogHome"),
    path("<int:sno>/<str:slug>/", views.blogPost, name="BlogPost"),
    path("postComment/", views.postComment, name="PostComment")
]
