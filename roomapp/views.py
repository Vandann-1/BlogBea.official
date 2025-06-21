from django.shortcuts import render
from blogapp.models import Blog
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseForbidden


# Create your views here.


# CREATE ROOM 

def join_discussion(request,blog_slug):
    blog = get_object_or_404(Blog, slug=blog_slug)
    if request.user != blog.user and not blog:
        return HttpResponseForbidden('Unauthorized Access!!')

    return render(request,'discus.html', {'blog':blog} )



from django.shortcuts import render, get_object_or_404
from .models import Blog  # import your Blog model

def blog_detail(request, slug):
    blog = get_object_or_404(Blog, slug=blog_slug)
    return render(request, 'discussion.html', {'blog': blog})

