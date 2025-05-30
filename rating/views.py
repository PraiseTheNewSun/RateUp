from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate
from django.contrib.auth.hashers import make_password
from django.contrib.auth.decorators import login_required
from .models import Post, Comment, Detail, ProfileImage
from .forms import PostForm, CommentForm, ProfileForm, SignUpForm, ProfileImageForm

# Create your views here.
def Home(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = make_password(request.POST.get('password'))
        user = Detail.objects.create(first_name=first_name, last_name=last_name, email=email, username=username, password=password)
        user.save()
        profile_photo = ProfileImage.objects.create(image_user=username)
        profile_photo.save()
        return redirect('login')
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
    posts= Post.objects.all()
    users= Detail.objects.get(username=posts.post_author)
    print(users)
    # user_list = []
    # for i in users:
    #     for j in posts:
    #         if j.post_author == i.username:
    #             print(i.first_name)
    #             user_list.append(i)
    try:
        photo = ProfileImage.objects.get(image_user=request.user)
        context = {
        'posts': Post.objects.all(),
        'photo': photo,
        'userss': user_list
        }
        return render(request, 'rating/dashboard.html', context)
    except Exception:
        context = {
        'posts': Post.objects.all(),
        }
        return render(request, 'rating/dashboard.html', context)

@login_required
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

@login_required
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
    image = []
    try:
        photo = ProfileImage.objects.get(image_user=request.user)
        image.append(photo)
        print('Successfull')
    except Exception:
        print('Not Found')
    if request.method == 'POST':
        print(request.POST)
        username  = request.POST.get('username')
        img = request.FILES['img']
        profile_photo = ProfileImage.objects.create(image_user=username, img=img)
        profile_photo.save()
        profile_form = ProfileForm(request.POST)
        print(request.POST, request.FILES['img'])
        if profile_form.is_valid():
            profile_form.save(img=request.FILES['img'])
    context = {
        'profile_form': ProfileForm(initial={'first_name': profile.first_name, 'last_name': profile.last_name, 'username': profile.username, 'email': profile.email}),
        'profile': profile,
        'photo': image[0] or image
    }
    return render(request, 'rating/profile.html', context)
