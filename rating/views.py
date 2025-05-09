from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from .models import Post, Comment, Detail
from .forms import PostForm, CommentForm, ProfileForm, SignUpForm, ProfileImageForm

# Create your views here.
def Home(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
    context = {
        'form': SignUpForm
    }
    return render(request, 'rating/home.html', context)

def Login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        try:
            auth_user = authenticate(username=username, password=password)
            if auth_user:
                login(request, auth_user)
                return redirect('dashboard')
        except Exception as e:
            print('User not found', e)
    return render(request, 'rating/login.html')

@login_required
def Dashboard(request):
    context = {
        'posts': Post.objects.all(),
    }
    return render(request, 'rating/dashboard.html', context)

def PostDetail(request, pk):
    post = Post.objects.get(id=pk)
    comment_form = CommentForm(initial={'author': request.user, 'post_caption': post.post_caption})
    if request.method == 'POST':
        form = CommentForm(request.POST)
        print(request.POST)
        if form.is_valid():
            form.save()

    context = {
        'post': Post.objects.get(id=pk),
        'comments': Comment.objects.filter(post_caption=post.post_caption),
        'form': comment_form
    }
    return render(request, 'rating/post_detail.html', context)

def CreatePost(request):
    post_form = PostForm(initial={'post_author': request.user})
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        
        if form.is_valid():
            form.save()
        print(request.POST)
        
    return render(request, 'rating/create_post.html', {'form': post_form})

@login_required
def ProfilePage(request):
    profile = Detail.objects.get(username=request.user)
    if request.method == 'POST':
        profile_form = ProfileForm(request.POST, request.FILES)
        print(request.POST, request.FILES)
        if profile_form.is_valid():
            profile_form.save()
    context = {
        'profile_form': ProfileForm(initial={'first_name': profile.first_name, 'last_name': profile.last_name, 'username': profile.username, 'email': profile.email}),
        'profile': profile,
        'profile_img': ProfileImageForm()
    }
    return render(request, 'rating/profile.html', context)