from django import forms

from .models import Blog


class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['title', 'content', 'image']


class CreateBlogForm(BlogForm):
    pass


class EditBlogForm(BlogForm):
    pass


class DeleteBlogForm(BlogForm):
    pass
