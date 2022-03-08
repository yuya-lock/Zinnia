from django import forms

from .models import Post


class PostCreateForm(forms.ModelForm):
    title = forms.CharField(label='タイトル')
    university = forms.CharField(label='大学名')
    body = forms.CharField(label='内容', widget=forms.Textarea)
    picture = forms.FileField(label='画像', required=False)

    class Meta:
        model = Post
        fields = ['title', 'university', 'body', 'picture']