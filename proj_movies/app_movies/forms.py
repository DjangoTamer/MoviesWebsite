from django import forms
from app_movies.models import Comment


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('user', 'email', 'text', 'to_whom')
