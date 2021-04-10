from django import forms
from .models import Post
class WritePost(forms.ModelForm):

    class Meta():
        model = Post
        fields = ('topic', 'title', 'description')