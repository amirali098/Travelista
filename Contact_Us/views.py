from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from Contact_Us.forms import ContactFormForm


def contact_us(request):
    if request.method == "GET":
        return render(request, 'Contact_us/contact.html')
    else:
        form=ContactFormForm(request.POST)
        if form.is_valid():
            form.instance.name = 'Anonymous'
            form.save()
            messages.success(request,"Success")
            return render(request, 'Contact_us/contact.html', {'form':form})
        else:
            messages.error(request,"Error")
            return HttpResponse("Failed")
