from django import forms
from bookapp.models import Post, Comment


class PostForm(forms.ModelForm):
    class Meta():
        model = Post
        fields = ('author', 'title', 'bookimg', 'integer', 'readpdf', 'audiofile', 'category', 'text')

        widgets = {
            'title': forms.TextInput(attrs={'class':'textinputclass'}),
            'text': forms.Textarea(attrs={'class':'editable medium-editor-textarea postcontent'})
        }



    

class CommentForm(forms.ModelForm):
    class Meta():
        model = Comment
        fields = ('author', 'text')

        widgets = {
            'author': forms.TextInput(attrs={'class':'textinputclass'}),
            'text': forms.Textarea(attrs={'class':'editable medium-editor-textarea postcontent'})
        }