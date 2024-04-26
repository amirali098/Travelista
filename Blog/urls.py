
from django.urls import path
from .views import *





urlpatterns = [
    path('', index ,name='index'),
    path('blog-home/',bloghome,name="bloghome"),
    path('blog-home/category/<str:cat>', bloghome, name="category"),
    path('blog-home/tags/<str:tag_names>', bloghome, name="tags"),
    path('blog-single/<int:pid>',blogsingle,name="blogsingle"),



]
