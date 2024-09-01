from django.shortcuts import render

# Create your views here.
def home_page(request):
    return render(request,"blog/index.html")


def postDetail(request,slug):
    return render(request,"blog/post-detail.html")

def postsList(request):
    return render(request,"blog/all-posts.html")

def authorDetail(request):
    pass