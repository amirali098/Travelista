

# Create your models here.
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.
class Category(models.Model):
    name=models.CharField(max_length=250)



    def __str__(self):
        return self.name

class posts(models.Model):

    title=models.CharField(max_length=250)
    content=models.TextField(max_length=250)
    author=models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    category=models.ManyToManyField(Category)
    create_date=models.DateTimeField(auto_now_add=True)
    published_date=models.DateTimeField(default=timezone.now)
    image=models.ImageField(upload_to='blog',default='blog/default.jpg')
    status=models.BooleanField(default=False)
    counted_views=models.IntegerField(default=0)

    def __str__(self):
        return self.title

    def test(self):
        return  'test'




