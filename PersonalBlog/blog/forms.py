from django import forms
from .models import Comment
from django.utils.translation import gettext_lazy as _

class CommentForm(forms.ModelForm):
    
    class Meta:
        model = Comment
        exclude = ["post","user"]
        labels = {
            
            "comment":_("Your comment:"),
        }
        
        help_texts = {
            "comment": _("What is your comment?."),
        }

