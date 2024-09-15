from django.contrib import admin

from .models import Author, Post, Tag

# Register your models here.
@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    search_fields = ["username"] 
    list_display = ["username",]
    list_filter = ["username"]


admin.site.register(Tag)

    
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug" : ("title",)}
    #list_filter = ["published","author","tags"]
    list_display = ["title","author","slug","image"]
    search_fields = ('title', 'author__username')

