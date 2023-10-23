from django.urls import path
from . import views 

urlpatterns = [
    path("", views.index, name="index"),
    path("posts", views.all_blog_posts, name="all_blog_posts"),
    path("posts/<str:slug>", views.full_blog_post, name="full_blog_post"),
]