

# Create your models here.
from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.models import User
from taggit.managers import TaggableManager

# Create your models here.
class Category(models.Model):
    name=models.CharField(max_length=250)



    def __str__(self):
        return self.name

class Post(models.Model):

    title=models.CharField(max_length=250)
    content=models.TextField(max_length=250)
    author=models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    category=models.ManyToManyField(Category)
    create_date=models.DateTimeField(auto_now_add=True)
    published_date=models.DateTimeField(default=timezone.now)
    image=models.ImageField(upload_to='blog',default='blog/default.jpg')
    status=models.BooleanField(default=False)
    counted_views=models.IntegerField(default=0)
    tags = TaggableManager()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return  reverse('blogsingle',kwargs={'pid':self.id})

    def test(self):
        return  'test'


class Comment(models.Model):

    name=models.CharField(max_length=250)
    email=models.EmailField()
    subject=models.CharField(max_length=250)
    message=models.TextField(max_length=250)
    post=models.ForeignKey(Post,on_delete=models.CASCADE)
    create_date=models.DateTimeField(auto_now_add=True)
    published_date=models.DateTimeField(default=timezone.now)
    approved=models.BooleanField(default=False)



    def __str__(self):
        return self.subject

    def get_absolute_url(self):
        return  reverse('blogsingle',kwargs={'pid':self.id})

    def test(self):
        return  'test'



