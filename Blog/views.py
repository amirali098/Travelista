
# Create your views here.
from django.contrib import messages
from django.http import Http404,HttpResponse
from django.shortcuts import render, get_object_or_404, redirect

from Blog.forms import CommentForm
from .models import Post, Comment
from django.utils import timezone
from django.core.paginator import Paginator
from taggit.models import Tag



# Create your views here.
def test(request):
    return render(request, 'Blog/blog-category.html')

def index(request):
    return render(request,'index.html')

from django.shortcuts import render

def coming_soon(request):
    return render(request, 'coming_soon.html')


def bloghome(request,cat=None, tag_names=None):
    post = Post.objects.filter(published_date__lte=timezone.now(),status=True)

    if cat:
        post=post.filter(category__name=cat)
    if  tag_names:
        post=post.filter(tags__name= tag_names)

    post = Paginator(post, 10)
    page = request.GET.get("page")
    post=post.get_page(page)
    context = {'posts': post}
    return render(request, 'Blog/blog-home.html', context)

def blogsingle(request,pid):
        if request.method == 'POST':
            form=CommentForm(request.POST)
            if form.is_valid():
                form.save()
            return redirect('blogsingle',pid=pid)
        else:
            #post = posts.objects.filter(published_date__lte=timezone.now(), status=True).get(id=pid)
            post = get_object_or_404(Post, published_date__lte=timezone.now(), status=True, id=pid)
            comments=Comment.objects.filter(post=post.id,approved=True)
            previous_post=Post.objects.filter(published_date__lte=timezone.now(), status=True).exclude(id__gte=pid).last()
            next_post=Post.objects.filter(published_date__lte=timezone.now(), status=True).exclude(id__lte=pid).first()
            post.counted_views+=1
            post.save()
            form = CommentForm()
            context = {'post': post,
                       'form':form,
                       'Comments':comments,
                       "previous_post":previous_post,
                       "next_post":next_post}
            return render(request, 'Blog/blog-single.html', context)
    # except :
    #      raise Http404("Post not found")



