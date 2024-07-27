from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import todo
from django.contrib.auth.decorators import login_required

@login_required
@login_required
def home(request):
    if request.method == 'POST':
        task = request.POST.get('task')
        due_date = request.POST.get('due_date')  # Get due_date from POST data
        if not task:
            messages.error(request, 'Task name cannot be empty.')
            return redirect('home-page')

        # Convert due_date to a datetime object if it's not empty
        if due_date:
            from datetime import datetime
            due_date = datetime.strptime(due_date, '%Y-%m-%dT%H:%M')  # Format: YYYY-MM-DDTHH:MM
        else:
            due_date = None

        new_todo = todo(user=request.user, todo_name=task, due_date=due_date)
        new_todo.save()
        return redirect('home-page')

    all_todos = todo.objects.filter(user=request.user)
    context = {
        'todos': all_todos
    }
    return render(request, 'todoapp/todo.html', context)


def register(request):
    if request.user.is_authenticated:
        return redirect('home-page')
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        if len(password) < 3:
            messages.error(request, 'Password must be at least 3 characters')
            return redirect('register')
        
        if User.objects.filter(username=username).exists():
            messages.error(request, 'Error, username already exists, use another.')
            return redirect('register')
        
        new_user = User.objects.create_user(username=username, email=email, password=password)
        new_user.save()

        messages.success(request, 'User successfully created, login now')
        return redirect('login')

    return render(request, 'todoapp/register.html', {})

def LogoutView(request):
    logout(request)
    return redirect('login')

def loginpage(request):
    if request.user.is_authenticated:
        return redirect('home-page')
    
    if request.method == 'POST':
        username = request.POST.get('uname')        
        password = request.POST.get('pass')
        
        validate_user = authenticate(username=username, password=password)
        if validate_user is not None:
            login(request, validate_user)
            return redirect('home-page')
        else:
            messages.error(request, 'Error, wrong user details or user does not exist')
            return redirect('login')

    return render(request, 'todoapp/login.html', {})

@login_required
def DeleteTask(request, name):
    try:
        get_todo = todo.objects.get(user=request.user, todo_name=name)
        get_todo.delete()
    except todo.DoesNotExist:
        pass
    return redirect('home-page')

@login_required
def Update(request, name):
    try:
        get_todo = todo.objects.get(user=request.user, todo_name=name)
        get_todo.status = True
        get_todo.save()
    except todo.DoesNotExist:
        pass
    return redirect('home-page')
