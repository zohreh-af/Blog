from django.contrib import admin

from .models import Author, Post, Tag

# Register your models here.
@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    search_fields = ["name"] 
    list_display = ["name",]
    list_filter = ["name"]


admin.site.register(Tag)


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug" : ("title",)}
    list_filter = ["published","author","tag"]
    list_display = ["title","author","slug"]
    
