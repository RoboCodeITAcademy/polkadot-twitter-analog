from django import forms
from .models import Post

class AddPostForm(forms.ModelForm):
    
    
    class Meta:
        fields = ()