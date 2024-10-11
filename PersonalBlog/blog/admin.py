from django.contrib import admin

from .models import  Post,Comment

# Register your models here.


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ("user","post")


#admin.site.register(Tag)

    
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug" : ("title",)}
    #list_filter = ["published","author","tags"]
    list_display = ["title","user","slug",]
    search_fields = ('title', 'user__username')

