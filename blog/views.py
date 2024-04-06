from django.shortcuts import redirect, render
from .forms import LoginForm ,SignUpForm,PostForm
from django.contrib.auth import authenticate, login as auth_login ,logout as auth_logout
from django.contrib.auth.models import User
from .models import Post
from django.contrib.auth.models import Group
# Create your views here.
 
def index(request):
    posts = Post.objects.all()
    return render(request,'home.html',{'posts':posts})

def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')

def login(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                auth_login(request, user)
                return redirect('dashboard')
            else:
                return render(request, 'login.html', {'form': form, 'error': 'Invalid Username or password'})
                
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})




def signup(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            confirm_password = form.cleaned_data['confirm_password']
            if User.objects.filter(username=username).exists():
                return render(request, 'signup.html', {'form': form, 'error': 'Username already taken'})
            if password != confirm_password:
                return render(request, 'signup.html', {'form': form, 'error': 'Passwords do not match'})
            user = User.objects.create_user(username=username, email=email, password=password, first_name=name)
            return redirect('dashboard')  
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})


def dashboard(request):
    if request.user.is_authenticated:
        posts = Post.objects.filter(username=request.user.username)
        return render(request,'dashboard.html',{'posts':posts})
    
    else:
        return redirect('login')

def logout(request):
    auth_logout(request)
    return redirect('home')

from django.shortcuts import render, redirect
from .forms import PostForm
from .models import Post

def add_post(request):
    if request.user.is_authenticated:
        form = PostForm(request.POST or None, request.FILES or None)
        if request.method == 'POST':
            if form.is_valid():
                title = form.cleaned_data['title']
                desc = form.cleaned_data['desc']
                img = form.cleaned_data['img']
                video = form.cleaned_data['video']
                username = request.user.username
                post = Post(title=title, desc=desc, username=username, img=img, video=video)
                post.save()
                form = PostForm()
                return redirect('dashboard')
        return render(request, 'addpost.html', {'form': form})
    else:
        return redirect('login')


    
def update_post(request,id):
    if request.user.is_authenticated:
        if request.method == 'POST':
            pi = Post.objects.get(pk=id)
            form = PostForm(request.POST,instance = pi)
            if form.is_valid():
                form.save()
                return  redirect('dashboard')
        else:
            pi = Post.objects.get(pk=id)
            form = PostForm(instance=pi)
        return render(request,'updatepost.html',{'form':form})
    else:
        return  redirect('login')
    
def delete_post(request,id):
    if request.user.is_authenticated:
        if request.method == 'POST':
            pi = Post.objects.get(pk=id)
            pi.delete()
        return redirect('dashboard')
    else:
        return  redirect('login')
    
