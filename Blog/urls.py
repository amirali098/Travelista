
from django.urls import path, re_path
from .views import *





urlpatterns = [
    re_path(r'^.*$', coming_soon),
    path('', index ,name='index'),
    path('blog-home/',bloghome,name="bloghome"),
    path('blog-home/category/<str:cat>', bloghome, name="category"),
    path('blog-home/tags/<str:tag_names>', bloghome, name="tags"),
    path('blog-single/<int:pid>',blogsingle,name="blogsingle"),



]
