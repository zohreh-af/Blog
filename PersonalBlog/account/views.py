from pyexpat.errors import messages
from django.http import HttpRequest
from django.http.response import HttpResponse as HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView,DetailView
#from .models import CostomUser as User
from blog.models import Post
from django.contrib import messages
from .forms import UserRegisterForm, UserLoginForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.mixins import LoginRequiredMixin


class UserRegisterView(View):
    class_form = UserRegisterForm
    class_template = "account/register.html"
    def dispatch(self, request, *args , **kwargs):
        if request.user.is_authenticated:
            return redirect('blog:home')
        return super().dispatch(request, *args, **kwargs)
    def get(self,request):
         form = self.class_form()
         return render(request,self.class_template,{'form':form})
    def post(self,request):
        form = self.class_form(request.POST)
        if form.is_valid():
            cd=form.cleaned_data
            User.objects.create_user(cd['username'],cd['email'],cd['password'])
            messages.success(request,"successfully signed up!!",'success')
            return redirect('account:login')
        return render(request,self.class_template,{'form':form}) 


class SignUpView(CreateView):
  
  def dispatch(self, request, *args, **kwargs):
      if request.user.is_authenticated:
          messages.error(request,"You have already registerd!")
          return redirect("account:profile") 
      return super().dispatch(request, *args, **kwargs)

  template_name = 'account/register.html'
  success_url = reverse_lazy('account:profile')
  form_class = UserRegisterForm
  success_message = "Your profile was created successfully"
    

class UserLoginView(View):
    class_form = UserLoginForm
    class_template = "account/login.html"
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect("account:profile",request.user.id)
        return super().dispatch(request, *args, **kwargs)
    
    def get(self,request):
        form = self.class_form()
        return render(request,self.class_template,{'form':form})
    
    def post(self,request):
        form = self.class_form(request.POST)
        if form.is_valid():
            cd=form.cleaned_data
            user = authenticate(request,username=cd['username'],password=cd['password'])
            if user is not None:
                login(request,user)
                messages.success(request,"successfully login",'success')
                return redirect('account:profile',user.id)
        messages.error(request," login failed!",'warning')
        return render(request,self.class_template,{'form':form}) 
    

class UserLogoutView(View):
    def get(self,request):
        logout(request)
        messages.success(request,"You Loged Out!","success")
        return redirect("account:login")



  
  
class ProfileView(LoginRequiredMixin,View):
    class_template = "account/profile.html"
    def get(self,request,user_id):
        user = get_object_or_404(User,pk=user_id)
        posts = user.posts.all()
        return render(request,self.class_template,{'posts':posts,"author":user})
    

# class ProfileView(LoginRequiredMixin,DetailView):
#     model = User
#     template_name = "account/profile.html"
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         #context["authors_posts"] = Post.objects.filter(author = self.id).order_by("-published")
#         context["posts"] = Post.authors.all().order_by("-published")
#         return context
