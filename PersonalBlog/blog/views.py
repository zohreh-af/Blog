
from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render
from django.views import View
from django.views.generic import DetailView,TemplateView,ListView,DeleteView
from .models import  Post,Tag
from .forms import CommentForm, CreatePostForm
from django.http import HttpRequest, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.models import User 
from django.utils.text import slugify
from django.contrib.auth.mixins import LoginRequiredMixin

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


# class PostDeleteView(DeleteView):
#     model = Post
#     template_name = "post_confirm_delete.html"
    
#     def delete(self, request, *args, **kwargs):
#         messages.success(request, 'The post was deleted successfully!')
#         return super().delete(request, *args, **kwargs)


class PostDeleteView(LoginRequiredMixin,View):
    def get(self,request,post_id):
        post = get_object_or_404(Post,pk=post_id)
        if post.user.id == request.user.id:
            post.delete()
            messages.success(request,"post deleted successfully!","success")
        else:
            messages.error(request,"you can not delete this post!")
        return redirect('blog:home')

class CreatePostView(LoginRequiredMixin,View):
    class_form = CreatePostForm
    class_template = "blog/create_post.html"
    def get(self,request):
        form = self.class_form
        return render(request,self.class_template,{'form':form})
    
    def post(self,request):
        form = self.class_form(request.POST)
        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.user = request.user
            new_post.slug = slugify(form.cleaned_data['title'])
            new_post.save()
            messages.success(request,"You added a new post!","success")
            return redirect('blog:post_detail',new_post.slug)
        messages.error(request,"try again!")
        return render(request,self.class_template,{'form':self.class_form})

class UpdatePostView(LoginRequiredMixin,View):
    class_form = CreatePostForm
    class_template = "blog/create_post.html"
    def setup(self, request: HttpRequest, *args, **kwargs) :
        self.post_instance = get_object_or_404(Post,pk=kwargs['post_id'])
        return super().setup(request, *args, **kwargs)
    
    def dispatch(self, request, *args, **kwargs):
        if not request.user.id == self.post.user.id:
            messages.error(request,"you are not allowed to edit this post!","danger")
            return redirect("blog:home")
        return super().dispatch(request, *args, **kwargs)
    
    def get(self,request, *args, **kwargs):
        post = self.post_instance
        form = self.class_form(instance=post)
        return render(request,self.class_template,{"form":form})

    def post(self,request, *args, **kwargs):
        post = self.post_instance
        form = self.class_form(request.POST,instance=post)
        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.user = request.user
            new_post.slug = slugify(form.cleaned_data['title'][:30])
            new_post.save()
            messages.success(request,"post updated successfully!","success")
            return redirect("blog:post_detail",post.slug)
        
        
        
