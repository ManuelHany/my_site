from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render, get_object_or_404
from django.http import Http404, HttpResponseNotFound, HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.views.generic import ListView, DetailView
from django.views import View

from collections import OrderedDict
from .models import Post
from .forms import CommentForm

class StartingPageView(ListView):
    model = Post
    template_name = "blog/index.html"
    context_object_name = "posts"
    ordering = ["-date"]
    
    def get_queryset(self):
        queryset = super().get_queryset()
        data = queryset[:3]
        return data


class PostsView(ListView):
    model = Post
    template_name = "blog/all-posts.html"
    context_object_name = "all_posts"
    ordering = ["-date"]


class PostDetailView(View):
    def get(seld, request, slug):
        post = Post.objects.get(slug=slug)
        context = {
            "post": post,
            "post_tags": post.tags.all(),
            "comment_form": CommentForm
        }
        return render(request, "blog/post-detail.html", context)
    
    def post(self, request, slug):
        comment_form = CommentForm(request.POST)
        post = Post.objects.get(slug=slug)

        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.save()
            return HttpResponseRedirect(reverse("post-detail-page", args=[slug]))
        
        context = {
            "post": post,
            "post_tags": post.tags.all(),
            "comment_form": comment_form
        }
        return render(request, "blog/post-detail.html", context)

