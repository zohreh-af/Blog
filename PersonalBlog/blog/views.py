from django.shortcuts import get_object_or_404, render

from PersonalBlog.blog.models import Author, Post

# Create your views here.
def home_page(request):
    post = Post.object.order_by('-updated')[:10]
    return render(request,"blog/index.html",{"posts":post})


def postDetail(request,slug):
    post = get_object_or_404(Post,slug)
    return render(request,"blog/post-detail.html",{"post":post})

def postsList(request):
    post = Post.object.order_by('-updated')
    return render(request,"blog/all-posts.html",{"posts":post})

def authorDetail(request,id):
    author = get_object_or_404(Author,id)
    post = Post.object.filter(author=author).order_by('-updated')[:10]
    return render(request,"blog/auther-detail.html",{"author":author,"posts":post})
