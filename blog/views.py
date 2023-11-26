from typing import Any
from django.shortcuts import render, get_object_or_404
from django.http import Http404, HttpResponseNotFound, HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.views.generic import ListView, DetailView

from collections import OrderedDict
from .models import Post

class StartingPageView(ListView):
    model = Post
    template_name = "blog/index.html"
    context_object_name = "posts"
    ordering = ["-date"]
    paginate_by = 3


class PostsView(ListView):
    model = Post
    template_name = "blog/all-posts.html"
    context_object_name = "all_posts"
    ordering = ["-date"]


class PostDetailView(DetailView):
    model = Post
    template_name = "blog/post-detail.html"
    context_object_name = "post"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["post_tags"] = self.object.tags.all()
        return context

