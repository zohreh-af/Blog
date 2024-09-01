from django.db import models
from django.urls import reverse
from django.core.validators import MaxValueValidator,MinValueValidator
# Create your models here.
class Author(models.Model):
    name = models.CharField( max_length=100,verbose_name="")
    email = models.EmailField( max_length=254,verbose_name="")
    
    class Meta:
        verbose_name = ("Author")
        verbose_name_plural = ("Authors")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("auther_detail", kwargs={"pk": self.pk})


class Post(models.Model):
    title = models.CharField(max_length=200,null=False,verbose_name="")
    author = models.ForeignKey("Author", verbose_name=(""), on_delete=models.CASCADE)
    slug = models.SlugField(default="",null=False)
    description = models.TextField()
    excrept = models.TextField(max_length=300)
    published = models.DateTimeField(auto_now=True, auto_now_add=True)
    updated = models.DateTimeField(auto_now=True, auto_now_add=True)
    score = models.FloatField(validators=[MinValueValidator(1),MaxValueValidator(5)])
    

    class Meta:
        verbose_name = ("پست")
        verbose_name_plural = ("پست ها")

    def __str__(self):
        return f"{self.title} - {self.author}"

    def get_absolute_url(self):
        return reverse("post_detail", kwargs={"pk": self.slug})
