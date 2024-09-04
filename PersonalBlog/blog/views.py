from django.shortcuts import get_object_or_404, render

from .models import Author, Post,Tag

# Create your views here.
def home_page(request):
    post = Post.object.order_by('-updated')[:3]
    return render(request,"blog/index.html",{"posts":post})


def postDetail(request,slug):
    post = get_object_or_404(Post,slug)
    return render(request,"blog/post-detail.html",
                  {"post":post,
                   "tags":post.tags.all(),
                   })

def postsList(request):
    post = Post.object.all().order_by('-updated')
    return render(request,"blog/all-posts.html",{"posts":post})

def authorDetail(request,id):
    author = get_object_or_404(Author,id)
    posts = Post.authors.all().order_by("-published")
    return render(request,"blog/auther-detail.html",{"author":author,"posts":posts})
