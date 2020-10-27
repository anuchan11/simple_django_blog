from django import forms
from blog.models import Post, Comments


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ("author", "title", "content")

        #widgets can be added to the input fiels of a form, for example text field is red color

        widgets = {
            'title':forms.TextInput(attrs={'class':'textinputclass'}),#textinputclass -- our css class
            'content':forms.Textarea(attrs={'class': 'editable medium-editor-textarea postcontent'}),  #text is connected to three CSS classes, postcontent is our defined css class
        }

class CommentsForm(forms.ModelForm):

    class Meta:
        model = Comments
        fields = ("author", "text")

        widgets = {
            'author': forms.TextInput(attrs={'class': 'textinputclass'}),
            'text':forms.Textarea(attrs={'class': 'editable medium-editor-textarea'}),
        }
