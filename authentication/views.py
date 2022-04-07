from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User

def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('index')
        else:
            messages.success(request, "There was an error!")
    return render(request, 'login.html', {
        "title":"Login"
    })

def register_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        first_name = request.POST["first_name"]
        last_name = request.POST["last_name"]
        email = request.POST["email"]
        password = request.POST["password"]
        confirm_password = request.POST["confirm_password"]

        if password == confirm_password:
            user = User.objects.create_user(
                username = username,
                first_name = first_name,
                last_name = last_name,
                email = email,
                password = password,
            )
            user.save()
            login(request, authenticate(request, username=username, password=password))
            messages.success(request, f'Welcome {username}!')
            return redirect('index')
        else:
            messages.warning(request, 'Password is not the same!')

    return render(request, 'register.html', {
        "title":"Register"
    })

def logout_user(request):
    logout(request)
    return redirect('index')

def delete_account(request):
    user_to_delete = User.objects.get(id=request.user.id)
    user_to_delete.delete()
    return redirect('login')