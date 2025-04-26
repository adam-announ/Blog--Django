from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Post
from .forms import PostForm, CommentaireForm

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, pk):
    template_name = 'blog/post_detail.html'
    post = get_object_or_404(Post, pk=pk)
    # récupération des commentaires signalés comme active
    commentaires = post.commentaires.filter(active=True)
    new_comment = None
    
    if request.method == 'POST':
        comment_form = CommentaireForm(data=request.POST)
        if comment_form.is_valid():
            # sauvegarder la data du formulaire sans faire de commit
            new_comment = comment_form.save(commit=False)
            # associer le nouveau commentaire avec le post en cours
            new_comment.post = post
            new_comment.save()
    else:
        comment_form = CommentaireForm()
    
    return render(request, template_name, {
        'post': post, 
        'commentaires': commentaires, 
        'new_comment': new_comment, 
        'comment_form': comment_form
    })

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.auteur = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})

def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.auteur = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})