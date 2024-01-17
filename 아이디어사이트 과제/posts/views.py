from django.shortcuts import render, redirect
from .forms import IdeaForm
from .models import IdeaItem

def idea_list(request):
    posts = IdeaItem.objects.all()
    ctx = {'posts': posts}
    return render(request, 'posts/idea_list.html', ctx)

def idea_submit(request):
    if request.method == 'POST':
        form = IdeaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        return redirect('posts:idea_list')
    else:
        form = IdeaForm()
        ctx = {'form' : form}
        return render(request, 'posts/idea_submit.html', context=ctx)
    
def idea_detail(request, pk):
    post = IdeaItem.objects.get(id=pk)
    ctx = {'post': post}
    return render(request, 'posts/idea_detail.html', context=ctx)

def idea_update(request, pk):
    post = IdeaItem.objects.get(id=pk)
    if request.method == 'POST':
        form = IdeaForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
        return redirect('posts:idea_list')
    else:
        form = IdeaForm(instance=post)
        ctx = { 'form' : form, 'pk' : pk}
        return render(request, 'posts/idea_update.html', ctx)
    
def idea_delete(request, pk):
    if request.method == 'POST':
        IdeaItem.objects.get(id=pk).delete()
    return redirect('posts:idea_list')