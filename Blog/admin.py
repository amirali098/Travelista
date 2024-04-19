from django.contrib import admin
from .models import posts,Category
# Register your models here.
admin.site.register(posts)
admin.site.register(Category)