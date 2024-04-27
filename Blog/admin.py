from django.contrib import admin
from .models import Post,Category,Comment
from django_summernote.admin import SummernoteModelAdmin
# Register your models here.



class PostAdmin(SummernoteModelAdmin):
    summernote_fields = '__all__'




admin.site.register(Post, PostAdmin)  # Here you register PostAdmin
admin.site.register(Category)
admin.site.register(Comment)