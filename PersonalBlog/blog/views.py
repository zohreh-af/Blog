from django.shortcuts import get_object_or_404, render
from django.views import View
from django.views.generic import DetailView,TemplateView,ListView
from .models import  Post,Tag
from .forms import CommentForm
from django.http import HttpResponseRedirect
from django.urls import reverse
from account.models import User as Author

class HomepageListView(ListView):
    template_name = "blog/index.html"
    model = Post
    context_object_name = "posts"
    ordering = ["-updated"]
    def get_queryset(self):
        queryset = super().get_queryset()
        data = queryset[:3]
        return data

    
class PostDetailView(View):
    
    def get(self,request,slug):
        favorite_id = request.session["fave_post"]
        post = Post.objects.get(slug=slug)
        is_favorite = favorite_id==str(post.id)
        context = {
            "post":post,
            "comment_form":CommentForm(),
            "post_tags":post.tags.all(),
            "comments":post.comments.all(),
            "is_favorite":is_favorite,
            
            }
        return render (request,"blog/post-detail.html.html",context)
    def post(self,request,slug):
        post = Post.objects.get(slug=slug)
        #post_id = request.POST["post_id"]
        request.session["fave_post"] = post.id
        context = {
            "post":post,
            "comment_form":CommentForm(),
            "post_tags":post.tags.all().order_by("-id"),
            
            }
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.save()
            return HttpResponseRedirect(reverse("post_detail",args=[slug]))
        return render (request,"blog/post-detail.html.html",context)
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context["comment_form"] = CommentForm()
    #     context["post_tags"] = self.object.tag.all()
    #     return context
    # #dont worry about slug :D 

class PostListView(ListView):
    model = Post
    ordering = ["-updated"]
    context_object_name = "posts"
    template_name = "blog/all-posts.html.html"
