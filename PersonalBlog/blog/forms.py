from django import forms
from .models import Comment
from django.utils.translation import gettext_lazy as _

class CommentForm(forms.ModelForm):
    
    class Meta:
        model = Comment
        exclude = ["post"]
        labels = {
            "username": _("Your username:"),
            "comment":_("Your comment:"),
        }
        error_messages = {
            "username": {
                "max_length": _("This username is too long."),

            },
        }
        help_texts = {
            "comment": _("What is your comment?."),
        }

