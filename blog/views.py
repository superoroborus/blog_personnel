from django.http import HttpResponseRedirect
from django.shortcuts import render
# Importation de la fonction render pour rendre les templates HTML

from blog.models import Post, Comment
# Importation des modèles Post et Comment depuis blog.models
from blog.forms import CommentForm

def blog_index(request):
    print("welcome to blogindex")
    # Vue pour la page d'index du blog
    posts = Post.objects.all().order_by("-created_on")
    # Récupère tous les posts de la base de données et les trie par date de création (les plus récents en premier)
    context = {
        "posts": posts,
    }
    # Crée un dictionnaire de contexte avec les posts
    return render(request, "blog/index.html", context)
    # Rend le template "blog/index.html" avec le contexte

def blog_category(request, category):
    # Vue pour la page des posts d'une catégorie spécifique
    posts = Post.objects.filter(
        categories__name__contains=category
    ).order_by("-created_on")
    # Filtre les posts par catégorie et les trie par date de création (les plus récents en premier)
    context = {
        "category": category,
        "posts": posts,
    }
    # Crée un dictionnaire de contexte avec la catégorie et les posts filtrés
    return render(request, "blog/category.html", context)
    # Rend le template "blog/category.html" avec le contexte

def blog_detail(request, pk):
    # Vue pour la page de détail d'un post spécifique
    post = Post.objects.get(pk=pk)
    # Récupère le post avec la clé primaire (pk) spécifiée
    form = CommentForm()
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = Comment(
                author=form.cleaned_data["author"],
                body=form.cleaned_data["body"],
                post=post,
            )
            comment.save()
            return HttpResponseRedirect(request.path_info)

    comments = Comment.objects.filter(post=post)
    # Filtre les commentaires associés à ce post
    context = {
        "post": post,
        "comments": comments,
        "form": CommentForm(),
    }
    # Crée un dictionnaire de contexte avec le post et ses commentaires
    return render(request, "blog/detail.html", context)
    # Rend le template "blog/detail.html" avec le contexte