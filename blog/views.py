# blog/views.py
from django.shortcuts import render, redirect
from .forms import PostForm
from .models import Post

def create_post_view(request):
    if request.method == 'POST':
        # CHANGED: Added request.FILES to bind file data to the form
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save() 
            return redirect('post_list') 
    else:
        form = PostForm()
        
    return render(request, 'create_post.html', {'form': form})

def post_list_view(request):
    posts = Post.objects.all().order_by('-created_at')
    return render(request, 'post_list.html', {'posts': posts})