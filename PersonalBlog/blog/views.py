from django.shortcuts import render

# Create your views here.
def home_page(request):
    return render(request,"blog/index.html")


def postDetail(request,slug):
    pass

def postsList(request):
    return render(request,"blog/all-posts.html")