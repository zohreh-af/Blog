from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
# class CostomUser(AbstractUser):
    
#     username = models.CharField( unique=True,max_length=50,null=True,verbose_name="یورزنیم ")
#     first_name = models.CharField( max_length=50,verbose_name="نام ")
#     last_name = models.CharField( max_length=50,verbose_name="نام خانوادگی")
#     email = models.EmailField( max_length=254,verbose_name="ایمیل")
#     def fullname(self):
#         return f"{self.first_name} {self.last_name}"

#     class Meta:
#         verbose_name = ("نویسنده")
#         verbose_name_plural = ("نویسنده ها")

#     def __str__(self):
#         return self.fullname()

#     def get_absolute_url(self):
#         return reverse("auther_detail", kwargs={"pk": self.id})


class Relations(models.Model):
    from_user = models.ForeignKey(User, verbose_name='follower', on_delete=models.CASCADE,related_name='follower')
    to_user = models.ForeignKey(User, verbose_name='following', on_delete=models.CASCADE,related_name='following')
    created = models.DateTimeField( auto_now_add=True)


    def __str__(self):
        f'{self.from_user} followed {self.to_user}'

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'Relation'
        verbose_name_plural = 'Relations'