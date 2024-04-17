from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .models import posts
from django.utils import timezone


# Create your views here.

def index(request):
    return render(request,'index.html')


def bloghome(request):
    post = posts.objects.filter(published_date__lte=timezone.now(),status=True)
    context = {'posts': post}
    return render(request,'blog-home.html',context)

def blogsingle(request,pid):
    post = posts.objects.get(pk=pid)
    context = {'post': post}
    return render(request,'blog-single.html',context)