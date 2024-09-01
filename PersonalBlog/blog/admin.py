from django.contrib import admin

from PersonalBlog.blog.models import Author

# Register your models here.
@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    prepopulated_fields ={"slug" : ("title",)}



admin.site.register(Author)
