from django import forms
from django.urls import reverse_lazy

from .models import Blog


class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ('title', 'content',)

        widgets = {
            'content': forms.Textarea(
                attrs={
                    'hx-post': reverse_lazy('preview'),
                    'hx-trigger': 'keyup changed delay:500ms',
                    'hx-target': '#preview',
                }
            )
        }
