from django.contrib import admin
#from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
from .models import Profile, Relations
from django.contrib.auth.models import User


admin.site.register(Relations)
class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False

class ExtendedUserAdmin(UserAdmin):
    inline = (ProfileInline)

admin.site.unregister(User)
admin.site.register(User,ExtendedUserAdmin)
