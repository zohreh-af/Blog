from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse
# Create your models here.
class User(AbstractUser):
    
    username = models.CharField( unique=True,max_length=50,null=True,verbose_name="یورزنیم ")
    first_name = models.CharField( max_length=50,verbose_name="نام ")
    last_name = models.CharField( max_length=50,verbose_name="نام خانوادگی")
    email = models.EmailField( max_length=254,verbose_name="ایمیل")
    def fullname(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
        verbose_name = ("نویسنده")
        verbose_name_plural = ("نویسنده ها")

    def __str__(self):
        return self.fullname()

    def get_absolute_url(self):
        return reverse("auther_detail", kwargs={"pk": self.id})

