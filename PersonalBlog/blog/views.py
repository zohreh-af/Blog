from django.shortcuts import get_object_or_404, render
from django.views.generic import DetailView,TemplateView,ListView
from .models import Author, Post,Tag


class HomepageListView(ListView):
    template_name = "blog/index.html"
    model = Post
    context_object_name = "posts"
    ordering = ["-updated"]
    def get_queryset(self):
        queryset = super().get_queryset()
        data = queryset[:3]
        return data
    
class PostDetailView(DetailView):
    model = Post
    template_name = "blog/post-detail.html.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["post_tags"] = self.object.tag.all()
        return context
    #dont worry about slug :D 
class PostListView(ListView):
    model = Post
    ordering = ["-updated"]
    context_object_name = "posts"
    template_name = "blog/all-posts.html.html"

class AuthorDetailView(DetailView):
    model = Author
    template_name = "blog/auther-detail.html.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        #context["authors_posts"] = Post.objects.filter(author = self.id).order_by("-published")
        context["authors_posts"] = Post.authors.all().order_by("-published")
        return context
    
