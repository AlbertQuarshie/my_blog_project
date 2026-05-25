# blog/forms.py
from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        # FIX: Added 'image' to the list
        fields = ['title', 'content', 'image'] 
        
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Enter post title...'}),
            'content': forms.Textarea(attrs={'placeholder': 'Write your story here...'}),
        }