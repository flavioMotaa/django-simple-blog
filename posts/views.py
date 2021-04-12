from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Post
from .forms import WritePost

# Create your views here.
def PostList(request):
    task_list = Post.objects.all()
    return render(request, 'posts/postlist.html', {'posts': task_list})
@login_required
def writePost(request):
    escreverPost = WritePost(request.POST)
    if request.method == "POST":
        if escreverPost.is_valid():
            post = escreverPost.save(commit=False)
            post.save()
            return redirect("/")
    return render(request, 'posts/addpost.html', {"form": escreverPost})

def readPost(request, id):
    post = get_object_or_404(Post, pk=id)
    return render(request, 'posts/postwritten.html', {"post": post, "id": id})
@login_required
def editPost(request, id):
    post = get_object_or_404(Post, pk=id)
    form = WritePost(instance=post)

    if request.method == "POST":
        form = WritePost(request.POST, instance=post)

        if(form.is_valid()):
            post.save()
            return redirect('/')
        else:
            return render(request, 'posts/editpost.html', {'form': form, 'post': post})
    else:
        return render(request, 'posts/editpost.html', {'form': form,'post': post})
@login_required
def deletePost(request, id):
    post = get_object_or_404(Post, pk=id)
    post.delete()
    return redirect("/")