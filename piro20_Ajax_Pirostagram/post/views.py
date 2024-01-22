from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
import json
from django.http import JsonResponse
from .forms import PostForm
from .models import Post, Comment

def main(request):
    search_txt = request.GET.get('search_txt')
    posts = Post.objects.all().order_by('-created_at')

    if search_txt:
        posts = posts.filter(title__icontains = search_txt)
    
    ctx = {'posts': posts} 
    return render(request, 'posts/main.html', context=ctx)

def create(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.post_user = request.user
            post.save() 
            return redirect('post:main')
    else:
        form = PostForm()
        ctx = {'form': form}
    return render(request, 'posts/create.html', ctx)

def detail(request, pk):
    post = Post.objects.get(id=pk)
    comments = post.comments.all()
    ctx = {'post': post, 'comments': comments}
    return render(request, 'posts/detail.html', ctx)

def update(request, pk):
    post = Post.objects.get(id=pk)
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
        return redirect('post:main')

    else:
        form = PostForm(instance=post)
        ctx = {'form': form, 'pk': pk}
        return render(request, 'posts/update.html', ctx)

def delete(request, pk):
    if request.method == 'POST':
        Post.objects.get(id=pk).delete()
    return redirect('post:main')

@csrf_exempt
def like(request):
    req = json.loads(request.body)
    post_id = req['id']

    post = Post.objects.get(id=post_id)
    post.like += 1
    post.save()

    return JsonResponse({'id': post_id})

@csrf_exempt
def comment(request):
    req = json.loads(request.body)
    post_id = req['id']
    comment_content = req['comment']

    pos = Post.objects.get(id=post_id)
    comment = Comment.objects.create(
        post = pos,
        author = request.user,
        content = comment_content
    )
    
    return JsonResponse({'id': comment.id, 'user': request.user.username, 'content': comment_content})
    
@csrf_exempt
def comment_delete(request):
    req = json.loads(request.body)
    comment_id = req['comment_id']

    comment = Comment.objects.get(id=comment_id)
    comment.delete()

    return JsonResponse({'id': comment_id})





