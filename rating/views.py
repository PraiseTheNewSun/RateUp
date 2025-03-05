from django.shortcuts import render
from .models import Post, Comment
from .forms import PostForm

# Create your views here.
def Home(request):
    if request.method == 'POST':
        post_author = request.POST.get('author')
        post_caption = request.POST.get('post_caption')
        post_comment = request.POST.get('comment')

        comment = Comment.objects.create(author=post_author, post_caption=post_caption, text=post_comment)


    context = {
        'posts': Post.objects.all(),
    }
    return render(request, 'rating/home.html', context)

def PostDetail(request, pk):
    context = {
        'post': Post.objects.get(id=pk),
        'comments': Comment.objects.all()
    }
    return render(request, 'rating/post_detail.html', context)

def CreatePost(request):
    if request.method == 'POST':
        # author = request.POST.get('post_author')
        # caption = request.POST.get('post_caption')
        # img = request.FILES
# 
        # post = Post.objects.create(post_author=author, post_caption=caption, post_img=img)
        # post.save()
        form = PostForm(request.POST, request.FILES)
        form.fields['post_author'].initial = 'Praise'

        if form.is_valid():
            form.save()
        print(request.POST)
        
    return render(request, 'rating/create_post.html', {'form': PostForm})