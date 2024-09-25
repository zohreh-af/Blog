from pyexpat.errors import messages
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views import View,TemplateView
from django.views.generic import CreateView
from .forms import UserRegisterForm, UserRegisterationForm
from django.contrib.auth.models import User

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
  template_name = 'account/register.html'
  success_url = reverse_lazy('account:dashboard')
  form_class = UserRegisterForm
  success_message = "Your profile was created successfully"
  



class DashboardView(TemplateView):
    template_name = "dashboard.html"
