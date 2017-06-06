# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.shortcuts import render, redirect

# Create your views here.
from blog.models import Post, Comment


def home(request):
    template_name = 'blog/home.html'
    posts = Post.objects.all()
    for i in posts:
        i.content = i.content[0:100] + "..."
    context = {'object_list': posts}
    return render(request, template_name, context)


def post_detail(request, id):
    template_name = "blog/post.html"
    post = Post.objects.get(id=int(id))
    comments = Comment.objects.filter(post=post)
    context = {'post': post, 'comments': comments}
    return render(request, template_name, context)


def add_post(request):
    if request.method == "POST":
        title = request.POST['title']
        content = request.POST['content']
        img = request.FILES['img']
        is_published = request.POST['is_published']
        user = User.objects.get(username=request.user.username)
        new_post = Post(title=title, user=user, content=content, img=img, is_published=is_published)
        new_post.save()
        return redirect('post', new_post.id)
    else:
        template_name='blog/add_post.html'
        context = {}
        return render(request, template_name, context)