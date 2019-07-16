from django import forms

from .models import Post

class PostForm(forms.ModelForm): # PostForm, ModelForm이라는 것을 알려주는 구문

    class Meta:
        model = Post
        fields = ('title', 'text',)
