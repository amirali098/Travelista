from django.utils import timezone
from django import template
from django.shortcuts import get_object_or_404
from Blog.models import posts,Category
from taggit.managers import TaggableManager
from taggit.models import Tag


register = template.Library()

#simple tag
@register.simple_tag
def Hi():
    return "test"

@register.simple_tag(name='plustwo')
def plus(a=2):
    return a+2


#{% post as t %}


@register.filter
def concat(values,arg=20):
    return values[:arg]

# {{ post.content|concat:1 }}


@register.inclusion_tag('Blog/blog-popularposts.html')
def popularpost(arg=3):
    # postss=get_object_or_404(posts, published_date__lte=timezone.now(), status=True).order
    postss=posts.objects.filter( published_date__lte=timezone.now(), status=True).order_by('published_date')[:arg]
    return {'posts':postss}



@register.inclusion_tag('Blog/blog-category.html')
def categories():
    postss=posts.objects.filter( published_date__lte=timezone.now(), status=True)
    categories=Category.objects.all()
    cat_dict = {}
    for name in categories:
        cat_dict[name]=postss.filter(category=name).count()
    return {'categories':cat_dict}


@register.inclusion_tag('index-recent-areaa.html')
def blog_recent():
    postss=posts.objects.filter( published_date__lte=timezone.now(), status=True).order_by('-published_date')
    return {'posts':postss}


@register.inclusion_tag('Blog/blog-tags.html')
def blog_tags(list=None):
    if list:
        tags=list
    else:
        tags=Tag.objects.all()

    return {'tags':tags}