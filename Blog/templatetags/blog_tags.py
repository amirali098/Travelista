from django.utils import timezone
from django import template
from django.shortcuts import get_object_or_404
from Blog.models import posts

register = template.Library()

#simple tag
@register.simple_tag
def Hi():
    return "test"

@register.simple_tag(name='plustwo')
def plus(a=2):
    return a+2


#{{ post as tp }}


@register.filter
def concat(values,arg=20):
    return values[:arg]

# {{ post.content|concat:1 }}


@register.inclusion_tag('blog-popularposts.html')
def popularpost(arg=3):
    # postss=get_object_or_404(posts, published_date__lte=timezone.now(), status=True).order
    postss=posts.objects.filter( published_date__lte=timezone.now(), status=True).order_by('published_date')[:arg]
    return {'posts':postss}