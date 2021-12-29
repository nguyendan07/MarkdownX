from django.shortcuts import get_object_or_404, render

from .models import Blog


def home(request):
    blogs = Blog.objects.all()
    return render(request, 'home.html', {'blogs': blogs})


def blog(request, slug):
    blog = get_object_or_404(Blog, slug=slug)
    return render(request, 'blog.html', {'blog': blog})
