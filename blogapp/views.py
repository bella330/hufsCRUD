from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Blog

def home(request):
    빈칸 = Blog.objects
    return render(request, 'home.html', {빈칸: 빈칸})

def detail(request, blog_id):
    빈칸 = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'detail.html', {빈칸: 빈칸})

def new(request):
    return render(request, 'new.html')

def create(request):
    blog = Blog()
    blog.title = request.POST[빈칸]
    blog.body = request.POST[빈칸]
    blog.pub_date = timezone.datetime.now()
    blog.save()
    return redirect('/blog/'+str(blog.id))

def delete(request, blog_id):
    destroy = get_object_or_404(Blog, pk=blog_id)
    destroy.delete()
    return redirect('home')

def update(request, blog_id):
    빈칸 = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'update.html', {빈칸: 빈칸})

def edit(request, blog_id):
    edit = Blog.objects.get(pk=blog_id)
    edit.title = request.POST[빈칸]
    edit.body = request.POST[빈칸]
    edit.pub_date = timezone.datetime.now()
    edit.save()
    return redirect('home')