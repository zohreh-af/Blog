from django import forms
from .models import Comment, Post
from django.utils.translation import gettext_lazy as _

class CommentForm(forms.ModelForm):
    
    class Meta:
        model = Comment
        fields = ('body',)
        labels = {
            
            "body":_("Your comment:"),
        }
        


class CreatePostForm(forms.ModelForm):
    #tags = forms.ModelMultipleChoiceField(queryset=Tag.objects.all(), widget=forms.CheckboxSelectMultiple, required=True)
    class Meta:
        model = Post
        fields = ("title","excrept","description")
class CommentReplyForm(forms.ModelForm):
            
    class Meta:
        model = Comment
        fields = ("body",)
        labels = {
            
            "body":_("Your reply to comment:"),
        }
        
class PostSearchForm(forms.Form):
    search = forms.CharField()