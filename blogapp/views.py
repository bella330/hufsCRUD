from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Blog

def home(request):
    빈칸 = Blog.objects
    return render(request, 'home.html', {"posts": 빈칸})

def detail(request, a):
    빈칸 = get_object_or_404(Blog, pk=빈칸)
    return render(request, 'detail.html', {빈칸: post})

def new(request):
    return render(request, 'new.html')

def create(request):
    blog = Blog()
    blog.title = request.POST[빈칸]
    blog.body = request.POST[빈칸]
    blog.pub_date = timezone.datetime.now()
    blog.save()
    return redirect('/blog/'+str(blog.id))

def delete(request, b):
    destroy = get_object_or_404(Blog, pk=빈칸)
    destroy.delete()
    return redirect('home')

def update(request, c):
    빈칸 = get_object_or_404(Blog, pk=빈칸)
    return render(request, 'update.html', {빈칸: text})

def edit(request, d):
    edit = Blog.objects.get(pk=빈칸)
    edit.title = request.POST[빈칸]
    edit.body = request.POST[빈칸]
    edit.pub_date = timezone.datetime.now()
    edit.save()
    return redirect('home')