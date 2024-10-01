from django import forms
from .models import Comment, Post, Tag
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

class CreatePostForm(forms.ModelForm):
    #tags = forms.ModelMultipleChoiceField(queryset=Tag.objects.all(), widget=forms.CheckboxSelectMultiple, required=True)
    class Meta:
        model = Post
        fields = ("title","excrept","description","image","tags")
