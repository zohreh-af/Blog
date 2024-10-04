from django.db import models
from django.urls import reverse
from django.core.validators import MaxValueValidator,MinValueValidator
from django.contrib.auth.models import User
class Tag(models.Model):
    caption = models.CharField(max_length=20)
    def __str__(self):
        return self.caption

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'تگ'
        verbose_name_plural = 'تگ ها'
        
class Post(models.Model):
    title = models.CharField(max_length=150,null=False,verbose_name="عنوان")
    user = models.ForeignKey(User, null=True ,verbose_name=("نویسنده"), on_delete=models.SET_NULL, related_name="posts")
    tags = models.ManyToManyField(Tag, verbose_name=("تگ"),)
    slug = models.SlugField(default="",null=False,unique=True,db_index=True,verbose_name="اسلاگ")
    excrept = models.TextField(max_length=300,verbose_name="تیتر دوم")
    description = models.TextField(verbose_name="متن")
    published = models.DateTimeField(auto_now_add=True,verbose_name="انتشار")
    updated = models.DateTimeField(auto_now=True,verbose_name="اپدیت" )
    image = models.ImageField(upload_to="update",verbose_name="ادرس عکس")
    

    class Meta:
        verbose_name = ("پست")
        verbose_name_plural = ("پست ها")

    def __str__(self):
        return f"{self.title} - {self.author}"

    def get_absolute_url(self):
        return reverse("blog:post_detail", kwargs={"slug": self.slug})

class Comment(models.Model):
    user = models.ForeignKey(User, null=True ,verbose_name=("نویسنده"), on_delete=models.SET_NULL, related_name="usercomments")
    post = models.ForeignKey(Post,related_name="postcomments" ,verbose_name=("پست "), on_delete=models.CASCADE)#manyToOne
    comment = models.TextField(verbose_name="متن کامنت")
    is_reply = models.BooleanField(verbose_name="پاسخ است؟")
    reply = models.ForeignKey('Comment', verbose_name='پاسخ', on_delete=models.CASCADE,related_name='')

    def __str__(self):
        return self.username - self.post__title

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'کامنت'
        verbose_name_plural = 'کامنت ها'

class Vote(models.Model):
    post = models.ForeignKey(Post, verbose_name='پست', on_delete=models.CASCADE,related_name='pvote')
    user = models.ForeignKey(User, verbose_name='کاربر', on_delete=models.CASCADE,related_name='uvote')
    def __str__(self):
        f'{self.user}-{self.post.slug}'

    class Meta:
        
        managed = True
        verbose_name = 'Vote'
        verbose_name_plural = 'Votes'