from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render,redirect,reverse





from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.views import *

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def save(self, commit=True):
        user = super(CustomUserCreationForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user



def signup(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            form = CustomUserCreationForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect(reverse('login'))
            else:
                return render(request, "Account/signup.html", {'form': form})  # You were not passing the form instance here
        else:
            form = CustomUserCreationForm()
            return render(request, "Account/signup.html", {'form': form})
    else:
        return redirect("/")

