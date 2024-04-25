from django.db import models

# Create your models here.


class ContactForm(models.Model):
    name = models.CharField(max_length=100)
    subject = models.CharField(max_length=100,null=True,blank=True)
    email = models.EmailField()
    message = models.TextField()