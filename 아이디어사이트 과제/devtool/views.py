from django.shortcuts import render, redirect
from .forms import devToolForm
from .models import devTool

def dev_list(request):
    posts = devTool.objects.all()
    ctx = {'posts': posts}
    return render(request, 'devtool/dev_list.html', ctx)

def dev_create(request):
    if request.method == 'POST':
        form = devToolForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('devtool:dev_list')
    else:
        form = devToolForm()
        ctx = {'form':form}
        return render(request, 'devtool/dev_create.html', ctx)
        

def dev_detail(request, pk):
    post = devTool.objects.get(id=pk)
    ctx = {'post': post}
    return render(request, 'devtool/dev_detail.html', ctx)

def dev_delete(request, pk):
    if request.method == 'POST':
        devTool.objects.get(id=pk).delete()
    return redirect('devtool:dev_list')

def dev_update(request, pk):
    post = devTool.objects.get(id=pk)
    if request.method == 'POST':
        form = devToolForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
        return redirect('devtool:dev_detail', pk=pk)
    else:
        form = devToolForm(instance=post)
        ctx = { 'form' : form, 'pk' : pk}
        return render(request, 'devtool/dev_update.html', ctx)

