from django.contrib import admin
from .models import posts,Category,ContactForm
# Register your models here.
admin.site.register(posts)
admin.site.register(Category)
admin.site.register(ContactForm)