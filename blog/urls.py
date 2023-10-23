from django.urls import path, include
from . import views 

posts_urls = [
    path("", views.all_blog_posts, name="all_blog_posts"),
    path("<str:slug>", views.full_blog_post, name="full_blog_post"),
]

urlpatterns = [
    path("", views.index, name="index"),
    path("posts/", include(posts_urls))
    
]