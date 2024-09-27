from pyexpat.errors import messages
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views import View,TemplateView
from django.views.generic import CreateView
from .forms import UserRegisterForm, UserRegisterationForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserLoginForm
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.mixins import LoginRequiredMixin
class UserRegisterView(View):
    class_form = UserRegisterationForm
    class_template = "account/register.html"

    def get(self,request):
         form = self.class_form()
         return render(request,self.class_template,{'form':form})
    def post(self,request):
        form = self.class_form(request.POST)
        if form.is_valid():
            cd=form.cleaned_data
            User.Objects.crea_user(cd['username'],cd['email'],cd['password'])
            messages.success(request,"successfully signed up!!",'success')
            return redirect('account:dashboard')
        return render(request,self.class_template,{'form':form}) 


class SignUpView(CreateView):
  
  def dispatch(self, request, *args, **kwargs):
      if request.user.is_authenticated:
          messages.error(request,"You have already registerd!")
          return redirect("account:dashboard") 
      return super().dispatch(request, *args, **kwargs)

  template_name = 'account/register.html'
  success_url = reverse_lazy('account:dashboard')
  form_class = UserRegisterForm
  success_message = "Your profile was created successfully"

  
  



class DashboardView(LoginRequiredMixin,TemplateView):
    template_name = "dashboard.html"


class UserLoginView(View):
    class_form = UserLoginForm
    class_template = "account/login.html"

    def get(self,request):
        form = self.class_form()
        return render(request,self.class_template,{'form':form})
    
    def post(self,request):
        form = self.class_form(request.POST)
        if form.is_valid():
            cd=form.cleaned_data
            user = authenticate(request,cd['username'],cd['email'],cd['password'])
            if user is not None:
                login(request,user)
                messages.success(request,"successfully login",'success')
                return redirect('account:dashboard')
        messages.error(request," login failed!",'warning')
        return render(request,self.class_template,{'form':form}) 
    

class UserLogoutView(View):
    def get(self,request):
        logout(request)
        messages.success(request,"You Loged Out!","success")
        return redirect("account:login")


