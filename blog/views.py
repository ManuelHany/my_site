from django.shortcuts import render
from django.http import Http404, HttpResponseNotFound, HttpResponseRedirect, HttpResponse
from django.urls import reverse
from collections import OrderedDict

# Create your views here.
def starting_page(request):
    return render(request, "blog/index.html")


def posts(request):
    return render(request, "blog/all-posts.html")


def post_detail(request, slug):
    slug_name = f"{slug}'s post"
    return render(request, 
                  "blog/blog.html", 
                  {
                      "slug_name": slug_name
                  })