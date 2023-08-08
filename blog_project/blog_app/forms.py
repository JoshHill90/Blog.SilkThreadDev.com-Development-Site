from django import forms
from .models import Blog, Category, Contact, Comments, MetaTags, EmailList
from django.core.exceptions import ValidationError
from blog_project.env.a1_fileter import Filtered

class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ('title', 'author', 'article', 'preview', 'category', 'image_url')
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Title for the post'}),
            'author': forms.TextInput(attrs={'class': 'form-control', 'value': '', 'id': 'userName', 'type': 'hidden'}),
            'article': forms.Textarea(attrs={'class': 'form-control'}),
            'preview' : forms.Textarea(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
            'image_url': forms.URLInput(attrs={'class': 'form-control'})
        }


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ('name', 'email', 'subject', 'body')
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your Name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Your Email'}),
            'subject': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Subject'}),
            'body' : forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Message Body'}),
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ('name', 'email', 'comment', 'user_id')


class EmailListForm(forms.ModelForm):
    class Meta:
        model = EmailList
        fields = ('email',)
        widgets = {
            'email': forms.EmailInput(attrs={'class': 'form-control',
                                             'style': 'max-width:300px',
                                             'placeholder': 'Your Email',
                                             'autocomplete': 'off'
                                             }),
        }