from django.shortcuts import (
    render, reverse, redirect, get_object_or_404)
from .models import Blog
from .forms import BlogForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required


def blog(request):
    blogs = Blog.objects.all()
    template = 'blog/blog.html'

    context = {
        'blog': blogs,
    }
    return render(request, template, context)

def blog_detail(request, blog_id):
    single_blog = get_object_or_404(Blog, pk=blog_id)

    context = {
        'blog': single_blog,
        'form': form,
    }
    return render(request, template, context)

@login_required()
def add_blog(request):
    if request.method == 'POST':
        form_data = {
                'blog_title': request.POST['blog_title'],
                'blog_author': request.POST['blog_author'],
                'blog_content': request.POST['blog_content'],
            }
        blog_form = BlogForm(form_data)
        if blog_form.is_valid():
            blog = blog_form.save()
            messages.success(request, 'New Blog content Added Successfully !')
            return redirect(reverse('add_blog'))
        else:
            messages.error(request, 'Failed to add Blog post. Please ensure the form is valid')
    else:
        form = BlogForm()

    template = 'blog/add_blog.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


