
# Create your views here.
from django.http import Http404
from django.shortcuts import render, get_object_or_404
from .models import posts
from django.utils import timezone


# Create your views here.
def test(request):
    return render(request,'blog-category.html')

def index(request):
    return render(request,'index.html')


def bloghome(request,cat=None):
    post = posts.objects.filter(published_date__lte=timezone.now(),status=True)
    if cat:
        post=post.filter(category__name=cat)
    context = {'posts': post}
    return render(request,'blog-home.html',context)

def blogsingle(request,pid):

        #post = posts.objects.filter(published_date__lte=timezone.now(), status=True).get(id=pid)
        post = get_object_or_404(posts, published_date__lte=timezone.now(), status=True, id=pid)
        previous_post=posts.objects.filter(published_date__lte=timezone.now(), status=True).exclude(id__gte=pid).last()
        next_post=posts.objects.filter(published_date__lte=timezone.now(), status=True).exclude(id__lte=pid).first()
        post.counted_views+=1
        post.save()
        context = {'post': post,
                   "previous_post":previous_post,
                   "next_post":next_post}
        return render(request,'blog-single.html',context)
    # except :
    #      raise Http404("Post not found")