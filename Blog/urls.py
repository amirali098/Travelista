
from django.urls import path
from .views import *

urlpatterns = [
    path('', index ,name='index'),
    path('blog-home',bloghome,name="bloghome"),
    path('blog-single/<int:pid>',blogsingle,name="blogsingle"),

]
