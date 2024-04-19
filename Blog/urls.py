
from django.urls import path
from .views import *

urlpatterns = [
    path('', index ,name='index'),
    path('blog-home',bloghome,name="bloghome"),
    path('blog-home/category/<str:cat>', bloghome, name="category"),
    path('blog-single/<int:pid>',blogsingle,name="blogsingle"),
    path('test',test,name="test"),

]
