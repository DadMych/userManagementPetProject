from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render

from .models import User


# display index page
def index(request):
    users = User.objects.all()
    return render(request, 'index.html', {"users": users})


# User creation
def create(request):
    if request.method == "POST":
        input_user = User()
        input_user.username = request.POST.get("username")
        input_user.first_name = request.POST.get("first_name")
        input_user.last_name = request.POST.get("last_name")
        input_user.email = request.POST.get("email")
        input_user.user_type = request.POST.get("user_type")
        input_user.password = request.POST.get("password")
        try:
            input_user.save()
            messages.success(request, f"{input_user.username} created")
        except Exception:
            messages.error(request, f"Error! Please try again!")
    return HttpResponseRedirect('/')


def retrieve(request, id):
    users = User.objects.all()
    current_user = User.objects.get(id=id)
    return render(request, 'index.html', {"current_user": current_user, "users": users})


def save(request, id):
    if request.method == "POST":
        current_user = User.objects.get(id=id)
        current_user.username = request.POST.get("username")
        current_user.first_name = request.POST.get("first_name")
        current_user.last_name = request.POST.get("last_name")
        current_user.email = request.POST.get("email")
        current_user.user_type = request.POST.get("user_type")
        current_user.password = request.POST.get("password")
        try:
            current_user.save(update_fields=['username', 'first_name', 'last_name', 'email', 'user_type', 'password'])
            messages.success(request, f"User updated successfully")
        except Exception:
            messages.error(request, f"Error! Please try again!")
    return HttpResponseRedirect('/')


def delete(request, id):
    if request.method == "POST":
        try:
            User.objects.filter(id=id).delete()
            messages.success(request, f"User successfully deleted")
        except Exception:
            messages.error(request, f"Error! Please try again!")
    return HttpResponseRedirect('/')
