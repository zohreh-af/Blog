
from typing import Any
from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render
from django.views import View
from django.views.generic import DetailView,TemplateView,ListView,DeleteView
from .models import  Post,Comment, Vote
from .forms import CommentForm, CommentReplyForm, CreatePostForm, PostSearchForm
from django.http import HttpRequest, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.models import User 
from django.utils.text import slugify
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


class HomepageListView(View):
    class_form = PostSearchForm
    def get(self,request):
        post = post.objects.all().order_by("-created")[:10]
        if request.GET.get('search'):
            post =  post.objects.filter(body__icontain=request.GET.get('search'))
        return render (request,'blog/index.html',{'posts':post,'form':self.class_form})
class PostDetailView(View):
    class_form = CommentForm
    class_form_reply = CommentReplyForm
    def setup(self, request, *args, **kwargs):
        self.post_instance = get_object_or_404(Post,kwargs['slug'])
        return super().setup(request, *args, **kwargs)
    def get(self,request, *args, **kwargs):
        #favorite_id = request.session["fave_post"]
        #is_favorite = favorite_id==str(post.id)
        comments = Post.pcomment.filter(is_reply=False)
        can_like = False
        if request.user.authenticated and self.post_instance.User_Have_Liked(request.user):
            can_like = True
    
        context = {
            "post":self.post_instance,
            "comment_form":self.class_form,
            "comment_reply_form":self.class_form_reply,
            "comments":comments,
            "can_like":can_like
            }
        return render (request,"blog/post-detail.html.html",context)
    @method_decorator(login_required)
    def post(self,request, *args, **kwargs):
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.user = request.user
            comment.post = self.post_instance
            comment.save()
            messages.success(request, 'your comment submitted successfully', 'success')
            return redirect('blog:post_detail',self.post_instance.slug)
# def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context["comment_form"] = CommentForm()
    #     context["post_tags"] = self.object.tag.all()
    #     return context
    # #dont worry about slug :D 
class PostAddReplyView(LoginRequiredMixin,View):
    class_form = CommentReplyForm
    def post(self,request,post_id,comment_id):
        post = get_object_or_404(Post,pk=post_id)
        comment = get_object_or_404(Comment,pk=comment_id)
        form = self.class_form(request.POST)
        if form.is_valid():
            reply = form.save(commit=False)
            reply.post = post
            reply.user = request.user
            reply.is_reply = True
            reply.reply = comment
            reply.save()
            messages.success(request, 'your reply submitted successfully', 'success')
        return redirect('blog:post_detail', post.slug)
class PostLikeView(LoginRequiredMixin,View):
    def Post(self,request,post_id):
        post = get_object_or_404(Post,pk=post_id)
        like = Vote.objects.filter(post=post,user=request.user)
        if like.is_exist():
            like.delete()
            messages.danger(request,"like retrived!","danger")
        else:
            Vote.object.create(post=post,user=request.user)
            messages.success(request,"yo liked the post!","success")
            return redirect ("blog:post_detail",post.slug)
class PostListView(ListView):
    model = Post
    ordering = ["-updated"]
    context_object_name = "posts"
    template_name = "blog/all-posts.html"


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
        
        
        
