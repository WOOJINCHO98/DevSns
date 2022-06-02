from django.shortcuts import redirect, render, get_object_or_404
from .models import Post
from forms import PostForm

# Create your views here.

def index(request):
    posts = Post.objects.all()
    return render(request, 'index.html', {'posts': posts})

def create(request):
    if request.method == 'POST': # 데이터를 전송
        # 받은 데이터로 새로운 게시물 생성
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        return redirect('index')
    else: # 처음 CREATE 페이지에 들어 왔을 때
        form = PostForm()
        return render(request, 'create.html',{'form': form})
    
def delete(request, id):
    post = get_object_or_404(Post, id = id)
    post.delete()
    return redirect('index')

def update(request, id):
    post = get_object_or_404(Post, id=id)
    if request.method == 'POST': # 데이터를 전송
        form = PostForm(request.POST, request.FILES, instance = post)
        if form.is_valid():
            form.save()
        return redirect('index')
    else: # c처음 update 페이지에 들어왔을 때 request.method == 'GET'
        form = PostForm(instance = post)
        return render(request, 'update.html', {'form':form, 'id':id})