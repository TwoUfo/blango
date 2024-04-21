from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from blog.models import Post


def index(request):
    posts = Post.objects.filter(published_at__lte=timezone.now())
    return render(request, "blog/index.html", {"posts": posts})
