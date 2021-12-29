from django.http.response import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render

from .forms import BlogForm
from .models import Blog


def home(request):
    blogs = Blog.objects.all()
    return render(request, 'home.html', {'blogs': blogs})


def blog(request, slug):
    blog = get_object_or_404(Blog, slug=slug)
    return render(request, 'blog.html', {'blog': blog})


def create(request):
    form = BlogForm()
    if request.method == 'POST':
        form = BlogForm(request.POST)
        if form.is_valid():
            blog = form.save()
            return redirect('create', slug=blog.slug)
        else:
            return render(request, 'create_blog.html', {'form': form, 'errors': form.errors})
    return render(request, 'create_blog.html', {'form': form, 'errors': None})\


def preview(request):
    content = request.POST['content']
    return HttpResponse(content)
